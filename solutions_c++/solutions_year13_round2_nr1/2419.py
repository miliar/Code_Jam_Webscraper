#include<stdio.h>
#include<fstream>
#include<algorithm>
#define SIZE 100
using namespace std;
int mote[SIZE];
int sol;
int n;
int find(int j,int a)
{
    int c=0;
    for(;j<n;j++)
        {
            if(a>mote[j])
                a+=mote[j];
            else if(a-1>0)
            {
                if(2*a-1>mote[j])
                {
                    c++;
                    a+=a-1+mote[j];
                }
                else
                {
                    int m=c+1+find(j,2*a-1),l=99999999;
                     l=c+1+find(j+1,a);
                    if(l>m) c=m;
                    else c=l;
                    return c;
                }
            }
            else
            {
                c=n;
            }
        }
        return c;
}

int main()
{
    int t,k=0;
    int a;
    ofstream ans;
    ifstream ques;
   // scanf("%d",&t);
   ques.open("in.txt");
   ans.open("out.txt");
 ques>> t;
    while(t--)
    {
        k++;
        sol=99999999;
      ques>> a>> n;
    //  scanf("%d %d",&a,&n);
        for(int i=0;i<n;i++)
        {
          ques>> mote[i];
      //  scanf("%d",mote+i);
        }
        sort(mote,mote+n);
        sol= find(0,a);
       ans<<"Case #" << k << ": "<<sol<<"\n";
      //  printf("%d\n",count);
    }
    ques.close();
    ans.close();
    return 0;
}
