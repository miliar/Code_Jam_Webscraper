#include <bits/stdc++.h>
#define gc getchar_unlocked
#define pc putchar

using namespace std;

inline int sn()
{
    char r;
	bool start=false,neg=false;
	int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

inline void wi(int n)
{
    int N = n, rev;
    int count = 0;
    rev = N;
    if (N == 0) { pc('0');  return ;}
    while ((rev % 10) == 0) { count++; rev /= 10;}
    rev = 0;
    while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}
    while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
    while (count--) pc('0');
}

int maneuver(char s[], int i){
    if(i < 0)return 0;
    int ans;
    if(s[i] == '-'){
        ans = 1;
        for(register int j = i - 1;j >= 0;j--){
            if(s[j] == '+'){
                ans += 1 + maneuver(s, j);
                break;
            }
        }
    }
    else{
        ans = 0;
        for(register int j = i - 1;j >= 0;j--){
            if(s[j] == '-'){
                ans = maneuver(s, j);
                break;
            }
        }
    }
    return ans;
}

int main(){
    int t = sn(), k = 1;
    char s[101];
    while(t--){
        scanf("%s",s);
        printf("Case #%d: %d\n", k++, maneuver(s, strlen(s) - 1));
    }
    return 0;
}
















