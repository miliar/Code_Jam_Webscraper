#include <iostream>
#include <algorithm>
using namespace std;
int T;
int answer;
int index;
int i;
int flag;//-1-wrong  0-multiple   1-16  right ansert 
int tmp;
int A1[17];
int B1[17];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xx.out","w",stdout);
    cin>>T;
    index=0;
    while(T--)
    {
       flag=-1;
       memset(A1,0,sizeof(A1));
       memset(B1,0,sizeof(B1));
       
       cin>>answer;
       for(i=0;i<16;i++)
       {
          cin>>tmp;
          if(((i/4)+1)==answer)
             A1[tmp]=answer;
       }
       
       cin>>answer;
       for(i=0;i<16;i++)
       {
          cin>>tmp;
          if(((i/4)+1)==answer)
             B1[tmp]=answer;
       }
       for(i=1;i<17;i++)
       {
          if(A1[i]!=0)
          {
             if(B1[i]!=0)
             {
                if(flag==-1)
                   flag=i;
                else 
                   flag=0;
             }
          }
       }
       
        index++;
        if(flag>=1&&flag<=16)
            cout<<"Case #"<<index<<": "<<flag<<endl;
         else if(flag==-1)
              cout<<"Case #"<<index<<": Volunteer cheated!"<<endl;
         else if(flag==0)
         cout<<"Case #"<<index<<": Bad magician!"<<endl;    
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
