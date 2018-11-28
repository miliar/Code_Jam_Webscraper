
#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

    int t;
    cin>>t;
    for(int f=1; f<=t; f++){
        string res = "";
        priority_queue< pair<int, char> > pq;
        int n, sum = 0;
        cin>>n;
        for(int i=0; i<n; i++){
            pair<int, int> p;
            cin>>p.first;
            sum += p.first;
            p.second = (char)(i + 'A');
            pq.push(p);
        }


        if(sum%2 == 1){
            pair<int, char> cur = pq.top();
            pq.pop();
            res += cur.second;
            res += " ";
            if(cur.first - 1 != 0)
                pq.push({cur.first - 1, cur.second});
        }

        while(!pq.empty()){
            pair<int, char> cur1 = pq.top();
            pq.pop();
            pair<int, char> cur2 = pq.top();
            pq.pop();


            res += cur1.second;
            res += cur2.second;
            res += " ";

            cur1.first--;
            cur2.first--;
            if(cur1.first > 0)
                pq.push(cur1);
            if(cur2.first > 0)
                pq.push(cur2);


        }
        cout<<"Case #"<<f<<": "<<res.substr(0, res.size()-1)<<endl;
    }
    return 0;
}

