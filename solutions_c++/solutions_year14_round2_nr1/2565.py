#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<bitset>
#include<iostream>

using namespace std;

char letter_seq[105];
int letter_seq_count = 0;

char s[105];
int counts[105][105];

int main() {
	int t, n,cs;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin>>t;
	
	for(int cs = 1; cs <=t ;++cs) {
		cin>>n;
		letter_seq_count = 0;
		
		int flag = false;
		
		for(int i = 0; i <n; ++i) {
			cin>>s;
			
			if(i == 0) {
				char last_letter = 0;
				int j = 0;
				for(; s[j] != 0; ++j) {
					if(s[j] != last_letter) {
						letter_seq[letter_seq_count++] = s[j];
						last_letter = s[j];
					}
				}
			}
			
			char last_letter = 0;
			int pointer_cnt = 0;
			int pointer_let =0;
			int cnt = 0;
			for(int j = 0; s[j] != 0; ++j) {
				if(s[j] != last_letter) {
					if(j != 0) {
						counts[i][pointer_cnt++] = cnt;
						
						if(last_letter != letter_seq[pointer_let]) {
							pointer_cnt = -1;
							break;
						}
						pointer_let++;
						
						cnt = 1;
					} else {
						cnt++;
					}
					last_letter = s[j];
				} else {
					cnt++;
				}
			}
			
			counts[i][pointer_cnt++] = cnt;
			if(last_letter != letter_seq[pointer_let]) {
				pointer_cnt = -1;
			}
			
			if(letter_seq_count != pointer_cnt) {
				flag = true;
				break;
			}
		}
		
		
		int ans = 0;
		
		for(int i = 0; i < letter_seq_count; ++i) {
			int sum = 0;
			for(int j = 0; j < n; ++j) {
				sum += counts[j][i];
			}
			
			int mean = sum / n;
			
			
			int dist = 0;
			
			for(int j = 0; j < n; ++j) {
				dist += abs(mean - counts[j][i]);
			}
			
			ans += dist;
		}
		
		
		if(flag) {
			printf("Case #%d: Fegla Won\n", cs);
		} else {
			printf("Case #%d: %d\n", cs, ans);
		}
	}
}
