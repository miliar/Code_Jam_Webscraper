#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream fout;
    fout.open("answer.txt");
    int t;
	cin>>t;
	int cnt=0;
	string s="",ans="";
	static int arr[26],dig[10];
	for(int i=1;i<=t;i++)
	{
	    cnt=0;
	    s="";
	    ans="";
	    cin>>s;
	    for(int j=0;j<s.length();j++)
	    {
	        arr[s[j]-65]++;
	    }
	    cnt=arr[23];
	    dig[6]+=cnt;
	    arr[23]-=cnt;
	    arr[18]-=cnt;
	    arr[8]-=cnt;

	    cnt=arr[25];
	    dig[0]+=cnt;
	    arr[25]-=cnt;
	    arr[4]-=cnt;
	    arr[17]-=cnt;
	    arr[14]-=cnt;

	    cnt=arr[6];
	    dig[8]+=cnt;
	    arr[6]-=cnt;
	    arr[4]-=cnt;
	    arr[8]-=cnt;
	    arr[7]-=cnt;
	    arr[19]-=cnt;

        cnt=arr[20];
        dig[4]+=cnt;
	    arr[20]-=cnt;
	    arr[5]-=cnt;
	    arr[14]-=cnt;
	    arr[17]-=cnt;

	    cnt=arr[22];
	    dig[2]+=cnt;
	    arr[22]-=cnt;
	    arr[19]-=cnt;
	    arr[14]-=cnt;

	    cnt=arr[18];
	    dig[7]+=cnt;
	    arr[18]-=cnt;
	    arr[4]-=cnt;
	    arr[4]-=cnt;
	    arr[21]-=cnt;
	    arr[13]-=cnt;

	    cnt=arr[19];
	    dig[3]+=cnt;
	    arr[19]-=cnt;
	    arr[7]-=cnt;
	    arr[17]-=cnt;
	    arr[4]-=cnt;
	    arr[4]-=cnt;

	    cnt=arr[14];
	    dig[1]+=cnt;
	    arr[14]-=cnt;
	    arr[13]-=cnt;
	    arr[4]-=cnt;

	    cnt=arr[5];
	    dig[5]+=cnt;
	    arr[5]-=cnt;
	    arr[8]-=cnt;
	    arr[21]-=cnt;
	    arr[4]-=cnt;

	    cnt=arr[8];
	    dig[9]+=cnt;
	    arr[8]-=cnt;
	    arr[13]-=cnt;
	    arr[13]-=cnt;
	    arr[4]-=cnt;

	    for(int x=0;x<10;x++)
	    {
	        while(dig[x]>0)
	        {
	            dig[x]--;
	            ans+=(char)(x+48);
	        }
	    }

	    fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	fout.close();
	return 0;
}