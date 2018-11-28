
/*
Sourav Bhattacharjee
IIT Kharagpur

GO
*/
#include <iostream>
#include <stdio.h>
using namespace std;

int getins(int n){

	int numcnt=0,cnt=1,num,temp;
    bool arr1[10]={false};
	if(n == 0)
		return -1;

	while(cnt<=150)
    {
		num=cnt*n;
		temp=num;

		while(temp>0)
        {
			int digit = temp%10;
			temp = temp/10;
			if(arr1[digit] == false)
			{
				arr1[digit] = true;
				numcnt++;
			}

		}
		if(numcnt>=10)
			return num;

		cnt++;

		if(cnt==150)
			return -1;

	}
}


int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

    int TestCase;
	cin >> TestCase;

	for(int i=1;i<=TestCase;i++)
	{
        int n,out;
        cin >> n;

		out=getins(n);

		if(out==-1)
			cout << "Case #" << i << ": "<< "INSOMNIA" << endl;
		else
            cout << "Case #" << i << ": "<< out << endl;

	}


    return 0;
}
