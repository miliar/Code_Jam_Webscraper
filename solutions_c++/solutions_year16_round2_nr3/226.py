#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <random>
#include <map>
#include <functional>
#include <string.h>
using namespace std;

void use_file(const std::string& s = "")
{
    if (s != "std" && s != "") {
        freopen((s+".in").c_str(), "r", stdin);
        freopen((s+".out").c_str(), "w", stdout);
    }
}

map<string, int> mpa, mpb;
vector<pair<int, int> > vp;


#define maxn 1001//��ʾx���Ϻ�y�����ж������������
 int nx,ny;//x���Ϻ�y�����ж���ĸ���
 int edge[maxn][maxn];//edge[i][j]Ϊ1��ʾij����ƥ��
 int cx[maxn],cy[maxn];//������¼x������ƥ���yԪ�����ĸ���
 int visited[maxn];//������¼�ö����Ƿ񱻷��ʹ���
 int path(int u)
 {
     int v;
     for(v=0;v<ny;v++)
     {
         if(edge[u][v]&&!visited[v])
         {
             visited[v]=1;
            if(cy[v]==-1||path(cy[v]))//���y�����е�vԪ��û��ƥ�������v�Ѿ�ƥ�䣬���Ǵ�cy[v]���ܹ��ҵ�һ������·
             {
                 cx[u]=v;
                 cy[v]=u;
                 return 1;
             }
         }
     }
     return 0;
 }

 int maxmatch()
 {
     int res=0;
     memset(cx,0xff,sizeof(cx));//��ʼֵΪ-1��ʾ���������ж�û��ƥ���Ԫ�أ�
     memset(cy,0xff,sizeof(cy));
     for(int i=0;i<=nx;i++)
     {
         if(cx[i]==-1)
         {
             memset(visited,0,sizeof(visited));
             res+=path(i);
         }
     }
     return res;
 }


int solve(int n){
    memset(edge, 0, sizeof(edge));
    memset(visited, 0, sizeof(visited));
    for (int i = 0; i < n; i++){
        edge[vp[i].first][vp[i].second] = 1;
    }
    nx = mpa.size();
    ny = mpb.size();
    return n - (nx + ny - maxmatch());
}

int main() {
    use_file("C2");
    int T, N;
    cin >> T;

    std::string a, b;
    for(int ca = 1; ca <= T; ca++){
        cin >> N;
        mpa.clear();
        mpb.clear();
        int ida = 0, idb  = 0;
        vp.clear();
        for (int i = 0; i < N; i++){
            cin >> a >> b;
            if (mpa.count(a) == 0){
                mpa[a] = ida++;
            }
            if (mpb.count(b) == 0){
                mpb[b] = idb++;
            }
            vp.push_back(make_pair(mpa[a], mpb[b]));
        }
        cout << "Case #" << ca << ": "  << solve(N) << std::endl;
    }
	return 0;
}
