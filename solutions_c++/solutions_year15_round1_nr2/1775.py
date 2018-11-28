#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <String>
#include <algorithm>
#include <queue>

using namespace std;
 
long long gcm(long long a, long long b)
{
	if (b == 0)	return a;
	else	return gcm(b, a%b);
}
long long lcm(long long a, long long b)
{
	return (a / gcm(a, b)) * b;
}

int main()
{
	freopen("output2.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTestCase = 0;
	cin >> nTestCase;

 	for (int  iTestCase = 1; iTestCase <= nTestCase; iTestCase++)
	{
		int nNode, nIndex, tTime = 0;;
		int barbor[2000] = { 0, };
		int answer = 0;
		long long tPeriod = 1;
		long long ttp = 0;
		priority_queue < pair<int, int> >  pii;

		cin >> nNode >> nIndex;
		for (int i = 1; i <= nNode; i++){
			cin >> barbor[i];
			pii.push(make_pair(-barbor[i], -i));
			tPeriod = lcm(tPeriod, barbor[i]);
			tTime = min(tTime, -barbor[i]);
		}
		//cout << "tPeriod	"<< nIndex << " " << nIndex% tPeriod << endl;
		for (int i = 1; i <= nNode; i++)
			ttp += tPeriod / barbor[i];
		if (nNode > nIndex)	answer = nIndex;
		else{
			nIndex -= nNode;
			nIndex = nIndex% ttp;
			answer = -nNode;
			for (int iCustomer = 0; iCustomer < nIndex; iCustomer++)
			{
			//	cout << "TOP " << -pii.top().first << " " << -pii.top().second << "			";
			//	cout << "PUSH " << -pii.top().first + barbor[-pii.top().second]<< " "<<-pii.top().second << endl;
				answer = pii.top().second;
				
				if (tTime == pii.top().first){
					pii.push(make_pair(pii.top().first - barbor[-pii.top().second], pii.top().second));
				}
				else
				{
					pii.push(make_pair(pii.top().first - barbor[-pii.top().second], pii.top().second));
					tTime = pii.top().first;
				}
				pii.pop();
			}
		}
		cout << "Case #" << iTestCase << ": " << -answer <<endl;
	}


	 
}