//best fit
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outputlarge.txt","w",stdout);
    int t;cin>>t;//cout<<t<<endl;
    int testcaseno=1;
    multiset <int,std::greater<int> > numbers;
    while(t--)
    {
        numbers.clear();
        int n,x,ele;
        cin>>n>>x;
        //cout<<n<<endl;
        for(int i=0;i<n;++i){cin>>ele;numbers.insert(ele);}
        //sort(numbers.begin(),numbers.end());
        //cout<<endl;
        multiset<int>::iterator it;
        //for (it = numbers.begin(); it != numbers.end(); it++)cout<<*it<<" ";cout<<endl;
        int sum_so_far=0;int nod=0;
        for (it = numbers.begin(); it != numbers.end(); )
        {
            multiset<int>::iterator it1=it;it1=++it1;
            multiset<int>::iterator temp;
            //cout<<*it<<" ";
            while(it1!=numbers.end())
            {
                if((*it+*it1)<=x)
                {
                    //cout<<*it1<<endl;
                    numbers.erase(it1);
                    break;
                }
                ++it1;
            }
            temp=it;temp=++temp;
            numbers.erase(it);
            it=temp;
            nod++;
        }
        cout<<"Case #"<<testcaseno<<": "<<nod<<endl;
        testcaseno++;
    }
    return 0;
}

