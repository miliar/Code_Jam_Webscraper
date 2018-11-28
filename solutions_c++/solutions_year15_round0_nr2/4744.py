#include <iostream>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <algorithm>
using namespace std;

bool Cable(priority_queue<int> x, int time)
{
    if(x.top() <= time) return true;
    if(time <= 1) return false;

    int num = 0;
    while(! x.empty())
    {
        if(x.top() > time)
            num++;
        else break;
        int y = x.top();
        x.pop();
        x.push((y + 1)/2);
        x.push(y/2);
    }
    return Cable(x, time - num);

}
//
//int main()
//{
////    freopen("B.txt","r",stdin);
//	freopen("B-small-attempt1.in","r",stdin);
//	freopen("B-small-attempt.out","w",stdout);
//	int T;
//	cin>>T;
//	for(int t = 1; t<= T; t++)
//	{
//		int D; cin>>D;
//        priority_queue<int> X;
//        for(int i = 0; i< D; i++)
//        {
//            int x; cin>>x;
//            X.push(x);
//        }
//        int high = X.top(); int low = 1;
//
//        while(low <high)
//        {
//            int med = (high + low)/2;
//            if(Cable(X, med))
//                high = med;
//            else
//                low = med+1;
//        }
////        cout<<low<<endl;
//		printf("Case #%d: %d\n", t, low);
//		//cout<<"Case #"<<t<<": "<<ret<<endl;
//	}
//}


int main()
{
//    freopen("B.txt","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t = 1; t<= T; t++)
	{
		int D; cin>>D;
        vector<int> X;
        for(int i = 0; i< D; i++)
        {
            int x; cin>>x;
            X.push_back(x);
        }
        sort(X.begin(), X.end());
        int high = X[X.size() - 1];
        int res = high;
        for(int time = 1; time <= high; time++)
        {
            int ret = 0;
            for(int i =0; i< X.size(); i++)
            {
                if(X[i] > time)
                {
                    if(X[i]%time == 0)
                        ret += X[i]/time -1;
                    else ret += X[i]/time;
                }
            }
            res = min(res, time + ret);
        }
//        int high = X.top(); inlt low = 1;
//
//        while(low <high)
//        {
//            int med = (high + low)/2;
//            if(Cable(X, med))
//                high = med;
//            else
//                low = med+1;
//        }
//        cout<<low<<endl;
		printf("Case #%d: %d\n", t, res);
		//cout<<"Case #"<<t<<": "<<ret<<endl;
	}
}


