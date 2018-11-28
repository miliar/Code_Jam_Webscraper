#include <iostream>
#include <algorithm>
using namespace std;
int T;
int index;
double result=0;
double c;
double f;
double x;
double f_my;
bool flag;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("xxlarge2.out","w",stdout);
    cin>>T;
    index=0;
    while(T--)
    {
        result=0;
        c=0;
        f=0;
        x=0;
        f_my=2;
        flag=false;
        
        cin>>c;
        cin>>f;
        cin>>x;
        index++;
        
        if(x<=c)
        {
           result=x/f_my; 
           printf("Case #%d: %.7f\n",index,result);
        }
        else
        {
            while(true)
            {       
                result+=c/f_my;
                if((x/(f_my+f)+result)<((x-c)/f_my+result))//如果买花费的时间少 
                {
                   f_my+=f;  
                }
                else
                {
                    break;
                }     
            }
            result+=(x-c)/f_my;
            printf("Case #%d: %.7f\n",index,result);
            //cout<<"Case #"<<index<<": "<<result<<endl;
        }
    }
   fclose(stdin);
   fclose(stdout);
    return 0;
}
