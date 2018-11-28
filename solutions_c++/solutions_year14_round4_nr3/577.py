#include<vector>
#include<cstdio>
#include<string.h>
#define FN 1000010 //點數
#define FM 1000010 //邊數
#define INF 1023456789 //視為無限大的值
using namespace std;
// E 是弧的 struct
// k 是該弧所連到的點
// c 是該弧的剩餘流量 
// 其中 es[2k] 和 es[2k+1] 儲存的弧一定是連相同兩點但方向相反的弧
// m 是對於編號為 id 的弧我們可知它是由點 es[id^1].k 連出去的
// 用此方法存弧可縮減記憶體使用量
struct E {
    int k,c;
    E(){}
    E( int _k, int _c ):k(_k),c(_c){}
} es[FM*2];

struct Flow {
    // n 為點數，m 為弧數
    // dis 為從源點藉由剩餘流量非零的弧到某點的最短距
    // e 記錄每個點連出去的弧的編號
    // 此程式碼限定源點為 0,匯點為 n-1

    int n,m,dis[FN],ptr[FN];
    int qq[FN],qr,ql;
    vector<int> e[FN];
    // init 為初始化函數
    void init( int _n ) {
        n=_n; m=0;
        for ( int i=0; i<n; i++ ) e[i]=vector<int>();
    }
    // 在網路流模型添加一條由 a 到 b 且流量限制為 c 的弧
    void add( int a, int b, int c ) {
        e[a].push_back(m); es[m]=E(b,c); m++;
        e[b].push_back(m); es[m]=E(a,0); m++;
    }
    // 使用 bfs 得到 dis 陣列的值
    bool BFS() {
        memset(dis,-1,n*sizeof(int));
        ql=qr=0;
        qq[qr++]=0;
        dis[0]=0;
        while ( ql!=qr && dis[n-1]==-1 ) {
            int p=qq[ql++];
            for(int i=0;i < (int)e[p].size(); i++) {
                E ee=es[ e[p][i] ];
                if ( ee.c==0 || dis[ee.k]!=-1 ) continue;
                dis[ee.k]=dis[p]+1;
                qq[qr++]=ee.k;
            }
        }
        return dis[n-1]!=-1;
    }
    // 回傳在分層圖中，找出一條從 p 出發流量不超過 c 的增廣路並回傳值
    int go( int p, int c ) {
        if ( p==n-1 ) return c;
        int tmp;
        // 若從 i=0 開始，也就是每次呼叫函式是都檢查該點所有連出的弧
        // 此演算法的時間複雜度仍會和 Edmonds-Karps Algorithm 一樣

        for(int i=ptr[p]; i<(int)e[p].size(); i++) {
            E &ee=es[e[p][i]];
            // 若剩餘流量為零或該弧不為分層圖上的弧就跳過
            if ( ee.c==0 || dis[p]+1!=dis[ee.k] ) continue;
            tmp=go(ee.k,min(c,ee.c));
            // 若能藉由該弧流到匯點，就回傳結果
            // 並設 ptr[p]=i 代表下次使用此函式直接從第 ptr[p] 個弧檢查就行了
            // 於是每條弧至多都只會出現一次檢查時沿該弧找不到增廣路的情形
            // 失誤的次數為 O(m), 而每次找到增廣路的弧數為 O(n)
            // 於是能確保每次在分層圖上找到所有最短增廣路的時間複雜度為 O(nm)

            if(tmp != 0){
                ee.c-=tmp; es[e[p][i]^1].c+=tmp;
                ptr[p]=i;
                return tmp;
            }
        }
        ptr[p] = (int)e[p].size();
        return 0;
    }
    // 此為求最大流的主函式
    int maxflow() {
        long long ret=0; // 儲存答案的變數

        // 每次要找所有最短增廣路之前
        // 先使用 bfs 以便知道哪些弧是分層圖上的弧
        // 並當已經無法從源點到匯點時結束 while 迴圈
        while ( BFS() ){
            for(int i=0;i<n;i++)ptr[i]=0;

            // 以 bfs 得到分層圖後一直找弧全在分層圖上的增廣路直到找不到為止
            // 由於每次找到增廣路後分層圖上至少會有一條弧剩餘流量減至 0
            // 故至多找到 O(m) 條增廣路
            while(true){
                int tmp=go(0,INF);
                if(tmp)ret+=tmp;
                else break;
            }
        }
        return ret;
    }
}flow;


int grid[105][505];

int main() {
	int T, nm= 1;
	int i, j, k;
	scanf("%d", &T);
	while (T--) {
		int w, h, b;
		scanf("%d%d%d", &w, &h, &b);
		for (i=1;i<=w;i++) {
			for (j=1;j<=h;j++) {
				grid[i][j]= 0;
			}
		}
		for (i=0;i<b;i++) {
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1++;
			y1++;
			x2++;
			y2++;
			for (j=x1;j<=x2;j++) {
				for (k=y1;k<=y2;k++) {
					grid[j][k]= 1;
				}
			}
		}
		flow.init(1000010);
		for (i=1;i<=w;i++) {
			for (j=1;j<=h;j++) {
				if (grid[i][j]==1) continue;
				flow.add(i*h+j, (h*w+100)+(i*h+j), 1);
				if (j!=h && !grid[i][j+1]) {
					flow.add((h*w+100)+(i*h + j),i*h + (j+1),1);
				}
				
				if (j!=1 && !grid[i][j-1]) {
					flow.add((h*w+100)+(i*h + j),i*h + (j-1),1);
				}
				
				if (i!=w && !grid[i+1][j]) {
					flow.add((h*w+100)+(i*h + j),(i+1)*h + j,1);
				}
				if (i!=1 && !grid[i-1][j]) {
					flow.add((h*w+100)+(i*h + j),(i-1)*h + j,1);
				}
			}
		}
		for (i=1;i<=w;i++) {
			flow.add(0, i*h+1, 1);
			flow.add((h*w+100)+(i*h+h), 1000009, 1);
		}
		int ans= flow.maxflow();
		
		printf("Case #%d: %d\n", nm++, ans);
	}
	return 0;
}
