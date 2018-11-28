#include<iostream>
#include<vector>
using namespace std;

int main()
{
    freopen("A_out.txt","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
    
    int TT;
    cin>>TT;
    
    for(int T = 1; T<=TT; T++)
    {
             
            
            int row1; 
            cin>>row1;
            row1--;
            int row1_val[4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            int x;
                            cin>>x;
                            if(i==row1)
                            {
                                row1_val[j] = x;
                            }
                    }
            }
            
            int row2; 
            cin>>row2;
            row2--;
            int row2_val[4];
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            int x;
                            cin>>x;
                            if(i==row2)
                            {
                                row2_val[j] = x;
                            }
                    }
            }
            vector<int> v;
            for(int i=0;i<4;i++)
            {
                    for(int j=0;j<4;j++)
                    {
                            if(row1_val[i]==row2_val[j])
                            {
                               v.push_back(row1_val[i]);
                            }
                    }
            }
            cout<<"Case #"<<T<<": "; 
            if(v.size() == 1)
            {
                        cout<<v[0]<<endl;
            }else if((v.size() > 1))
            {
                  cout<<"Bad magician!"<<endl;
            }else
            {
                 cout<<"Volunteer cheated!"<<endl;
             }
    }
    
    return 0;
    
}
