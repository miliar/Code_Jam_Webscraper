#include <iostream>
#include <algorithm>
#include <fstream>
#include <deque>

using namespace std;

int main()
{
    freopen("B-small-attempt9.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int tt=1; tt<=t; tt++)
    {
        int x,n,minn=0,c=0,cc=0;
        cin>>n;
        deque<int>deq;
        deque<int>deqq;
        for (int i=0; i<n; i++)
        {
            cin>>x;
            deq.push_back(x);
        }
        deqq=deq;
        sort(deq.begin(),deq.end());
        sort(deqq.begin(),deqq.end());
        minn=deq.back();
        while (true)
        {
            c++;
            if (c==25) break;
            if (deq.back()==9) { deq.back()=6; deq.push_back(3); }
            else if (deq.back()==7) { deq.back()=4; deq.push_back(3); }
            else if (deq.back()==5) { deq.back()=3; deq.push_back(2); }
            else if (deq.back()==3) { deq.back()=2; deq.push_back(1); }
            else if (deq.back()==1) { deq.back()=1; deq.push_back(0); }
            else if (deq.back()==2) { deq.back()=1; deq.push_back(1); }
            else if (deq.back()==4) { deq.back()=2; deq.push_back(2); }
            else if (deq.back()==6) { deq.back()=3; deq.push_back(3); }
            else if (deq.back()==8) { deq.back()=4; deq.push_back(4); }
            sort(deq.begin(),deq.end());
            if (deq.back()+c<minn)
            {
                minn=deq.back()+c;
            }
        }
        while (true)
        {
            cc++;
            if (cc==25) break;
            if (deqq.back()==9) { deqq.back()=4; deqq.push_back(5); }
            else if (deqq.back()==7) { deqq.back()=4; deqq.push_back(3); }
            else if (deqq.back()==5) { deqq.back()=3; deqq.push_back(2); }
            else if (deqq.back()==3) { deqq.back()=2; deqq.push_back(1); }
            else if (deqq.back()==1) { deqq.back()=1; deqq.push_back(0); }
            else if (deqq.back()==2) { deqq.back()=1; deqq.push_back(1); }
            else if (deqq.back()==4) { deqq.back()=2; deqq.push_back(2); }
            else if (deqq.back()==6) { deqq.back()=3; deqq.push_back(3); }
            else if (deqq.back()==8) { deqq.back()=4; deqq.push_back(4); }
            sort(deqq.begin(),deqq.end());
            if (deqq.back()+cc<minn)
            {
                minn=deqq.back()+cc;
            }
        }
        cout<<"Case #"<<tt<<": "<<minn<<endl;
    }
    return 0;
}
