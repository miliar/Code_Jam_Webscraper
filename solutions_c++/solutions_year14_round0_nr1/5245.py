#include <iostream>
#include <string>
#include <vector>
using namespace std;
int my_compare(vector<int> a,vector<int> b,int o)
{
    int res=0;
    int ans=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            if(a[i]==b[j])
            {
                res++;
                ans=a[i];
                }
    }
    if(res==0)
        cout<<"Case #"<<o+1<<": "<<"Volunteer cheated!"<<endl;
                else if(res==1)
                    cout<<"Case #"<<o+1<<": "<<ans<<endl;
                    else
                        cout<<"Case #"<<o+1<<": "<<"Bad magician!"<<endl;
    return res;
}
int main()
{
    unsigned int num;
    cin>>num;

    vector<vector<int>>  data;
    for(unsigned int k=0;k<2*num;k++)
    {
        int id;
        cin>>id;
        for(int h=0;h<4;h++)
        {
            vector<int> temp;

            for(int t=0;t<4;t++)
            {
                int input;
                cin>>input;
                temp.push_back(input);
            }

            if(h==id-1)
               data.push_back(temp);
        }

    }
    for(unsigned int x=0;x<num;x++)
    {
        int r=my_compare(data[2*x],data[2*x+1],x);



    }

    return 0;
}

