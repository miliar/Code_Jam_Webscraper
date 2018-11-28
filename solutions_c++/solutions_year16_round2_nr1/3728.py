#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {

int t,g=1;
cin >> t;

while(t--)
{

	string s;
	cin >> s;

    int arr[2000],k=0;
    for(int i=0;i<2000;i++)
        arr[i]=15;
	int count[26]={0};

	for(int i=0;i<s.length();i++)
		count[(int)s[i]-65]++;

	while(count[(int)'Z'-65]>0)
	{
		count[(int)'Z'-65]--;
		count[(int)'E'-65]--;
		count[(int)'R'-65]--;
		count[(int)'O'-65]--;
		arr[k]=0;
		k++;
	}
	while(count[(int)'W'-65]>0)
	{
		count[(int)'W'-65]--;
		count[(int)'T'-65]--;
		count[(int)'O'-65]--;
		arr[k]=2;
		k++;
	}
	while(count[(int)'U'-65]>0)
	{
		count[(int)'F'-65]--;
		count[(int)'O'-65]--;
		count[(int)'U'-65]--;
		count[(int)'R'-65]--;
		arr[k]=4;
		k++;
	}
	while(count[(int)'X'-65]>0)
	{
		count[(int)'S'-65]--;
		count[(int)'I'-65]--;
		count[(int)'X'-65]--;
		arr[k]=6;
		k++;
	}
	while(count[(int)'G'-65]>0)
	{
		count[(int)'E'-65]--;
		count[(int)'I'-65]--;
		count[(int)'G'-65]--;
		count[(int)'H'-65]--;
		count[(int)'T'-65]--;		
		arr[k]=8;
		k++;
	}

	while(count[(int)'O'-65]>0)
	{
		count[(int)'O'-65]--;
		count[(int)'N'-65]--;
		count[(int)'E'-65]--;
		arr[k]=1;
		k++;
	}


	while(count[(int)'T'-65]>0)
	{
		count[(int)'T'-65]--;
		count[(int)'H'-65]--;
		count[(int)'R'-65]--;
		count[(int)'E'-65]--;
        count[(int)'E'-65]--;
		arr[k]=3;
		k++;
	}
	while(count[(int)'F'-65]>0)
	{
		count[(int)'F'-65]--;
		count[(int)'I'-65]--;
		count[(int)'V'-65]--;
		count[(int)'E'-65]--;
		arr[k]=5;
		k++;
	}
	while(count[(int)'S'-65]>0)
	{
		count[(int)'S'-65]--;
		count[(int)'V'-65]--;
		count[(int)'N'-65]--;
		count[(int)'E'-65]--;
		count[(int)'E'-65]--;
		arr[k]=7;
		k++;
	}
	while(count[(int)'N'-65]>0)
	{
		count[(int)'N'-65]--;
		count[(int)'N'-65]--;
		count[(int)'I'-65]--;
		count[(int)'E'-65]--;
		arr[k]=9;
		k++;
	}
    sort(arr,arr+2000);
    cout << "Case #"<<g++<<": ";    
    for(int i=0;i<2000;i++)
    {
      if(arr[i]!=15)
        cout<< arr[i];
      else
          break;
    }
    cout << endl ;
}
    return 0;
}