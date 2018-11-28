#include <iostream>
#include<vector>
using namespace std;

int main()
{
   int t;
   cin>>t;
   for(int q=1;q<=t;q++)
   {
        int last;
        vector<int>dones;
        for(int i=0;i<10;i++)
        {

            dones.push_back(i);
        }
        int n;
        cin>>n;
        if(n==0)
            last=-1;
        else
        {
            int i=1;
            while(dones.size()>0)
            {
                int x=n*i;
                while(x>0)
                {
                    for(int j=0;j<dones.size();j++)
                    {
                        if(dones[j]==x%10)
                        {
                            //cout<<x%10<<endl;
                            if(dones.size()==1)
                                last=n*i;
                            dones.erase(dones.begin()+j);
                            break;
                        }

                    }
                    x/=10;
                }
                i++;
            }
        }
        if(last==-1)
        {
            cout<<"Case #"<<q<<": INSOMNIA"<<endl;
        }
        else
            cout<<"Case #"<<q<<": "<<last<<endl;

   }
    return 0;
}
