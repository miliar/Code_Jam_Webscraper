#include<fstream.h>                //------------------------------------------------------------//
#include<stdio.h>                  //  ___  ___ _____ ______                                     //
#include<algorithm>                //  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //
#include<math.h>                   //  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
#include<vector.h>                 //  | |\/| | `--. \| ___ \                                    //
#include<set.h>                    //  | |  | |/\__/ /| |_/ /    Email: manish05@facebook.com    //
#include<map.h>                    //  \_|  |_/\____/ \____/                                     //
#include<string.h>                 //------------------------------------------------------------//

         

#define gc getchar_unlocked
#define MEM(a,b) memset(a,(b),sizeof(a))
#define FOR(i,n) for(int i=(0);i<(n);i++)
#define CLEAR(a) memset((a),0,sizeof(a))
#define S(n) scanf("%d", &n)
#define P(k) printf("%d\n", k)
#define fastS(n) scanint(&n)
#define pb push_back
#define mp make_pair
#define ll long long
#define VI vector<int>
#define PII pair<int, int>
#define ft first
#define sd second
#define inf (1<<30)
#define PNL printf("\n")
#define SP system("pause")
#define md 1000000007
#define PII pair<int, int>
#define mxx 1000000000
#define swap(a,b) {*b = (*a + *b) - (*a = *b);}


int n,m,a[101][101];
int row(int i)
{
    int t=a[i][0];
    for(int j=0;j<m;j++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int column(int j)
{
    int t=a[0][j];
    for(int i=0;i<n;i++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int main()
{

ifstream fin;fin.open("data.in",ios::in);
ofstream fout;fout.open("data.out",ios::out);

    int test=0,jkl=1;
    fin>>test;
    while(test--){
                  int trace=1;
                  fin>>n>>m;
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  fin>>a[i][j];
                  int max=a[0][0];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]>max) max=a[i][j];
                  int to[101][101];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  to[i][j]=max;
                  for(int i=0;i<n;i++)
                  if(row(i)==1) {
                                int tem=a[i][0];
                                for(int j=0;j<m;j++)
                                to[i][j]=tem;
                                }
                  for(int j=0;j<m;j++)
                  {
                          if(column(j)==1) {
                                           int tem=a[0][j];
                                           for(int i=0;i<n;i++)
                                           to[i][j]=tem;
                                           }
                  }
                  
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]!=to[i][j]) {trace=0;break;}
                  
                  if(trace==1) fout<<"Case #"<<jkl<<": YES"<<endl;
                  else fout<<"Case #"<<jkl<<": NO"<<endl;
                  jkl++;}

   fin.close();
   fout.close();
    return 0;
}
