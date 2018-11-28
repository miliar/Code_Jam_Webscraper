#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
using namespace std;

//vector<int> v;
//
//int main()
//{
//	int T;
//	scanf("%d",&T);
//	for(int k=0;k<T;++k)
//	{
//		int n,s;
//		scanf("%d%d",&n,&s);
//		v.clear();
//		v.resize(n);
//		for(int i=0;i<n;++i)
//			scanf("%d",&v[i]);
//		sort(v.begin(),v.end());
//		int c=0;
//		while(!v.empty())
//		{
//			int M=v.back();
//			v.pop_back();
//			if(v.empty())
//			{
//				++c;
//				break;
//			}
//			vector<int>::iterator it=lower_bound(v.begin(),v.end(),M);
//			if(it!=v.end())
//			{
//				if(s-M>=*it)
//					v.erase(it);
//			}
//			++c;
//		}
//		printf("Case #%d: %d\n",k+1,c);
//	}
//
//	return 0;
//}





int main ()
{
    ios_base::sync_with_stdio(0);
	freopen("D:\\int.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, cap;
        cin >> n >> cap;
        vector <int> files (n);
        for (int j = 0; j < n; ++j)
            cin >> files[j];
        vector <char> used(n);
        int cnt = 0;
        std::sort (files.begin(), files.end());
		reverse(files.begin(),files.end());
        for (int j = 0; j < n; ++j)
        {
            if (used[j]) continue;
            for (int k = j + 1; k < n ; ++k)
            {
                if (used[k]) continue;
                if (files[j] + files[k] <= cap)
                {
                    used[j] = 1;
                    used[k] = 1;
                    break;
                }
            }
            ++cnt;
        }
        cout << "Case #" << i + 1 << ": " << cnt << endl;
    }
}