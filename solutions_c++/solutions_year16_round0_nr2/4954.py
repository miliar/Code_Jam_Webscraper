#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("pancake_in.txt", "r", stdin);
    freopen("pancake_out.txt", "w", stdout);
	int t;
	cin >> t;
	int m=t;
	while(t--) {
        string s;
        cin >> s;
        int count = 0;
        for(int i=0;i<s.length()-1;i++) {
            if(s[i] != s[i+1])
                count++;
        }
        if(s[s.length()-1] == '-')
            count++;
		printf("Case #%d: %d\n",m-t,count);
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
