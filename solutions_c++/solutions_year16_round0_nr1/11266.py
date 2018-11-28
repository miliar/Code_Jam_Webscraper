#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("mmm.txt","r",stdin);
    freopen("kk.txt","w",stdout);
    int t,temp,mini,temp1;
    string s;
    //bool flag=true;
    int arr2[11];

    //vector<long long>arr;
    long long int type;
    scanf("%d",&t);
    /*ifstream in;
    in.open("inputItem.txt");

    ofstream out;
    out.open("outputItem.txt");*/
    for(int i=1; i<=t; i++)
    {
    	memset(arr2,0,sizeof(arr2));

        cin>>temp;
        stringstream ss;

        for(int l=1; l<=200; l++)
        {
            type=temp*l;
            ss<<type;
            s=ss.str();
            for(int j=0; j<s.size(); j++)
            {
                temp1=s[j]-'0';
                //cout<<temp1<<endl;
                arr2[temp1]++;
            }


           mini = *std::min_element(arr2,arr2+10);
           //cout<<mini<<endl;
            if(mini>=1)
			{
				break;
			}


        }
        if(mini==0)
		{
			printf("Case #%d: INSOMNIA\n",i);
			//cout<<"Case #"<<i<<: INSOMNIA"<<endl;
		}
		else
			printf("Case #%d: %lld\n",i,type);
			//cout<<"Case #i: "<<type<<endl;


        }




    return 0;
}
