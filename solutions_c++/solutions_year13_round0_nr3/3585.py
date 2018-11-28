#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

/*int  squareRoot(int  n)
{
  /*We are using n itself as initial approximation
   This can definitely be improved
   int ans;
  float x = (float)n;
  float y = 1;
  float e = 0.000001; /* e decides the accuracy level
  while(x - y > e)
  {
    x = (x + y)/2;
    y = n/x;
  }
  ans=(int)x;
  return ans;
}*/
int check(int n)
{
    int q,w;
    q=n;
    w=0;
    while(q!=0)
    {
        w=(w*10)+(q%10);
        q=q/10;
    }
    //printf("%d %d",q)
    //cout<<w<<" "<<n<<"\n";
    //return 0;
    if(w==n)
    return 1;
    return 0;
}
int main()
{
    int t,ans,n1,n2,r,cou,i,u;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t;
    for(u=1;u<=t;u++)
    {
        fin>>n1>>n2;
        cou=0;
        for(i=n1;i<=n2;i++)
        {
            r=check(i);
            if(r==1)
            {
                ans=sqrt(i);
                if(ans*ans==i)
                {
                    r=check(ans);
                    if(r==1)
                    {
                        //cout<<i<<"palindrome\n";
                        cou++;
                    }
                }
            }
            //cout<<i<<"  ";
        }
        fout<<"Case #"<<u<<": "<<cou<<"\n";
    }
    return 0;
}
