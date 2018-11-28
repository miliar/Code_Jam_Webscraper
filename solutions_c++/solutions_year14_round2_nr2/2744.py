# include <iostream>

using namespace std;


int main()
{
    int t, a, b, k, cases =0;

    cin >>t;

    for (cases ; cases<t ; ++cases)
    {
    a=0;b=0;k=0;
        cin >> a>>b>>k;
        int ans=0;
        for(int i=0;i<a;++i)
        {
            for (int j=0;j<b;++j)
            {
            int ord = i&j;
           // cout<<endl<<ord<<endl;
                if (  ord <k        )
                {

                    ++ans;
                    //cout<<"   i  = "<<i<<"  j = "<<j<<"   "<<b;
                }
            }
        }



    cout<<"Case #"<<cases+1<<": "<<ans<<endl;





    }




return 0;
}
