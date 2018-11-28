#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	int z; cin>>z; for(int x=0; x<z; x++)
	{
		int n; cin>>n;
		priority_queue<int> q;
		priority_queue<int> q1;

		for(int i=0; i<n; i++)
			{int k; cin>>k; q.push(k);q1.push(k); }

		int k =0; int w = q.top();

		//int a = q.top();
		while(q.top() > 2)
		{
			//cerr<<q.top()<<endl;
			w = min (w, q.top() + k);

			k++;
			int a = q.top();
			q.pop();
			q.push(a/2);
			if(a%2==0)
				q.push(a/2);
			else
				q.push(a/2 + 1);
		}

		w = min (w, q.top() + k);

		swap(q, q1);

		if(q.top() == 9)
		{
			k = 2;
			q.pop();
			q.push(3); q.push(3);q.push(3);

			while(q.top() > 2)
			{
				//cerr<<q.top()<<endl;
				w = min (w, q.top() + k);

				k++;
				int a = q.top();
				q.pop();
				q.push(a/2);
				if(a%2==0)
					q.push(a/2);
				else
					q.push(a/2 + 1);
			}

			w = min (w, q.top() + k);

		}



		cout<<"Case #"<<x+1<<": "<<w<<endl;

	}

	return 0;
}