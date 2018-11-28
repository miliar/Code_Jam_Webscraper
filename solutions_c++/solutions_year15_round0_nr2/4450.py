#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        int nonempty;
        cin >> nonempty;
        priority_queue <int, vector<int>, less<int> > pq;
        for(int j=0; j<nonempty; j++)
        {
            int plate;
            cin >> plate;
            pq.push(plate);
        }
        int a=0;
        if(pq.top() == 9)
        {
            pq.pop();
            if(pq.top()<=3 || pq.empty())
                a=1;
            else if(pq.top() == 6)
            {
                int temp = pq.top();
                pq.pop();
                if(pq.empty())
                    a=1;
                else if(pq.top()<=3)
                    a=1;
                pq.push(temp);
            }
            pq.push(9);
        }
        int ans=pq.top(), move_time=0;
        while(1)
        {
            int temp = pq.top();
            if(temp>3)
            {
                pq.pop();
                move_time++;
                pq.push(temp/2);
                pq.push(temp-temp/2);
            }
            else break;
            if(move_time+pq.top() < ans)
                ans = move_time+pq.top();
        }
        if(a==1) ans--;
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
