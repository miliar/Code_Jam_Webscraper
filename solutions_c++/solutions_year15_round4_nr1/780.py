#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    int t,i,j,k;
    char in[1005][1005];
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d\n",&t);
    for(int cnt = 1;cnt<=t;cnt++){
        int n,m;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
            scanf("%s",in[i]);
        //for(i=0;i<n;i++)
        //    printf("%s\n",in[i]);
        int imp = 0;
        for(i=0;i<n;i++)for(j=0;j<m;j++)if(in[i][j]!='.'){
            int sum = 0;
            for(int l=0;l<n;l++)if(in[l][j]!='.')
                sum++;
            for(int l=0;l<m;l++)if(in[i][l]!='.')
                sum++;
            //printf("%d %d %d\n",i,j,sum);
            if(sum == 2){
                imp = 1;
                i = n;
                j = m;
            }
        }
        if(imp){
            printf("Case #%d: IMPOSSIBLE\n", cnt);
            continue;
        }
        int ret = 0;
        int vst[105][105];
        memset(vst,0,sizeof(vst));
        for(i=0;i<n;i++)for(j=0;j<m;j++)if(in[i][j]!='.'&&vst[i][j] == 0){
            int r = i, c = j;
            while((r>=0&&r<n&&c>=0&&c<m)&&!vst[r][c]){
                //printf("s%d %d\n",r,c);
                vst[r][c] = 1;
                if(in[r][c] == '^'){
                    for(r=r-1;r>=0;r--)
                        if(in[r][c] != '.')
                            break;
                }else if(in[r][c] == 'v'){
                    for(r=r+1;r<n;r++)
                        if(in[r][c] != '.')
                            break;
                }else if(in[r][c] == '<'){
                    for(c=c-1;c>=0;c--)
                        if(in[r][c] != '.')
                            break;
                }else{
                    for(c=c+1;c<m;c++)
                        if(in[r][c] != '.')
                            break;
                }
            }
            //printf("e%d %d\n",r,c);
            if(!(r>=0&&r<n&&c>=0&&c<m))
                ret += 1;
        }

        printf("Case #%d: %d\n", cnt, ret);
    }
    return 0;
}
