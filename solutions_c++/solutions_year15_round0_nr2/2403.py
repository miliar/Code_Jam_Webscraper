#include <bits/stdc++.h>
using namespace std;
vector<int> plate;


int solve(int diners,int maxi)
{
    int i,temp1=0,kk=maxi,j;
    //cout<<"1\n";
    for(i=1;i<=maxi;i++)
    {
        //cout<<"3\n";
        temp1=i;
        for(j=0;j<diners;j++)
        {
            //cout<<"4\n";
            if(plate[j]>i)
            {
                //cout<<"6\n";
                if(plate[j]%i!=0)
                    temp1=temp1+(plate[j]/i);
                else if(plate[j]%i==0)
                    temp1=temp1+(plate[j]/i-1);
                //cout<<"5\n";
            }
        }
        kk=min(kk,temp1);
    }
   // cout<<"2\n";
    return kk;
}

int main()
{
    int i,temp=0,t,diners,k=1,ans=0;
    cin>>t;
    while(t--)
    {
        int tk=-1;
        plate.clear();
        cin>>diners;
        for(i=0;i<diners;i++)
        {
            cin>>temp;
            plate.push_back(temp);
            if(tk<temp)
                tk=temp;
        }
        //sort(plate.begin(),plate.end());
        //for(i=0;i<plate.size();i++)
          //cout<<plate[i]<<" ";
        //cout<<"ewret"<<endl;


        if(diners==1 && plate[0]==1)
            ans=1;
        else if(tk==2)
            ans=2;
        else
            ans=solve(diners,tk);

        cout<<"Case #"<<k<<": "<<ans<<endl;
        k++;
    }
    return 0;
}
