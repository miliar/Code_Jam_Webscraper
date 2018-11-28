#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    int tc1=1;
    int a,b,k;
    FILE *fp1, *fp2;
  //  fp1 = fopen("small.in", "r");
    fp2 = fopen("ans3.txt", "w");
    while(tc1<=tc)
    {
                  int cnt=0;
                cin>>a>>b>>k;
                for(int i=0;i<a;i++)
                {for(int j=0;j<b;j++)
                if((i&j)<k)
                {
                           cnt++;
                           //cout<<i<<j<<endl;
                           
                }
                }
                fprintf(fp2,"Case #%d: %d\n",tc1,cnt);
                tc1++;
    }
    return 0;
}
