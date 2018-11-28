using namespace std;
#include<iostream>
int main()
{
    int i,j,t,s_max,y=0,countp=0;
    string p;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>s_max;
        int num[s_max+1];
        countp=0;
        y=0;
        cin>>p;
        for(j=0;j<=s_max;j++)
        {
            num[j]=p[j]-'0';
            //cout<<num[j]<<" ";
            if(countp<j)
            {
                y+=(j-countp);
                countp+=(j-countp);
            }
        countp+=num[j];
        }
        cout<<"Case #"<<(i+1)<<": "<<y<<endl;
        y=0;
        s_max=0;
    }
    return 0;
}
