#include<iostream>
#include<vector>
using namespace std;
int main()
{
     freopen("/Users/saravanakumars/program1.txt","r",stdin);
    freopen("/Users/saravanakumars/program1.out","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,c;
        cin>>n;
        vector<int> v(n);
        int containsFive = 0,containsSix = 0,onlyNine = 1;

        //cout<<"init v"<<endl;
        for(int j=0;j<n;j++)
        {
            cin>>c;
            v.push_back(c);
            if(c == 5)
            {
                containsFive = 1;
            }
            if(c == 6)
            {
                containsSix = 1;
            }
            if(c != 9 || j>0)
            {
                onlyNine = 0;
            }
           // cout<<c<<" ";
        }
        //cout<<endl;
        make_heap(v.begin(),v.end());
        int time = 0;
        while(true)
        {
            if(v.front() <= 1)
            {
                break;
            }
            int s = v.size() - 1;
            int temp = v.front();
            int count = 0;
            while(v.front() == temp)
            {
                pop_heap(v.begin(),v.end());
                v.pop_back();
                count++;
            }
            int newMax = 0;
            /*cout<<"size is "<<v.size()<<endl;
            for(int k=0;k<v.size();k++)
            {
                cout<<"k is "<<k<<v[k];
            }
            cout<<endl;*/
           // if(v.size() > 1)
            //{
                 newMax = v.front();
            //}
            //else
            if(v.front() == 0)
            {
                newMax = temp - temp/2;
            }
            //cout<<"front is "<<temp<<" count is "<<count<<" temp/2 is "<<temp/2<<endl;
            //cout<<"newMax + count is "<<newMax+count<<" temp is "<<temp<<" newMax is "<<newMax<<endl;
           // if(temp/2 <= count)
           if(newMax+count>temp)
            {
                v.push_back(temp);
                push_heap(v.begin(),v.end());
                break;
            }
            time +=count;
            for(int k=0;k<count;k++)
            {
                if(temp != 9)
                {
                     v.push_back(temp/2);
                  push_heap(v.begin(),v.end());
                  v.push_back(temp - temp/2);
                  push_heap(v.begin(),v.end());
                }
                else
                {
                    if(containsSix || onlyNine)// || (!containsFive && !containsSix))
                    {
                         v.push_back(3);
                  push_heap(v.begin(),v.end());
                  v.push_back(6);
                  push_heap(v.begin(),v.end());
                    }
                    else
                    {
                         v.push_back(4);
                  push_heap(v.begin(),v.end());
                  v.push_back(5);
                  push_heap(v.begin(),v.end());
                    }

                }

            }
            //sort_heap(v.begin(),v.end());
         /*   cout<<"time "<<time<<":";
            for(int k=0;k<v.size();k++)
            {
                cout<<v[k]<<" ";
            }
            cout<<endl;*/
        }
        time += v.front();
        cout<<"Case #"<<(i+1)<<": "<<time<<endl;
    }
}
