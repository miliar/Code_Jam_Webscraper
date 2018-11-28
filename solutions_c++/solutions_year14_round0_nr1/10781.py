
#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<cstring>
#include<algorithm>
#include<cmath>
#define print1(a) printf("%d\n",a);
#define print2(a,b) printf("%d %d\n",a,b);
#define print3(a,b,c) printf("%d %d %d\n",a,b,c);
#define all(c) c.begin(),c.end();
#define loop(i,n) for(i=0;i<n;i++)
typedef long long int ll;
using namespace std;
long long int get()
{
	  char c;
	  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
	  long long int flag=(c=='-');
	  if(flag)
	    c=getchar();
	  long long int x=0;
	  while(c>='0'&&c<='9')
	    {
	      x=x*10+c-48;
	      c=getchar();
	    }
  return flag?-x:x;
}
int main()
{
    int t;
    ifstream inp;
    ofstream out;
    inp.open("C:\\Users\\krishanakant\\Desktop\\A-small-attempt1.in");
    out.open("C:\\Users\\krishanakant\\Desktop\\my.txt");
    inp>>t;
    int w=1;
    while(t--)
    {
        int p;
        inp>>p;
        int arr[5][20]={0};
         int arr1[5][20]={0};
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int x;
                inp>>x;
                arr[i][x]++;
            }
        }
        int q;
        inp>>q;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int y;
                inp>>y;
                arr1[i][y]++;
            }
        }
        int c=0;
        int count=0;
        for(int i=0;i<20;i++)
        {
          if(arr1[q][i]==1&&arr[p][i]==1){
                count++;
                c=i;
          }
        }
        if(count==0)
            out<<"Case #"<<w++<<": "<<"Volunteer cheated!\n";
        else if(count==1)
            out<<"Case #"<<w++<<": "<<c<<"\n";
        else
            out<<"Case #"<<w++<<": "<<"Bad magician!\n";

    }
    return 0;
}
