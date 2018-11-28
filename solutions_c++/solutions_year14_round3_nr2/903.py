#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::string str[101];
int N;
int answer;
std::string compact(const char *str){
	std::string outstr = "";
	if (str == NULL || str[0] == 0) return outstr;
	char prev = str[0];
	outstr += prev;
	for (int i = 1; str[i] != 0; i++){
		if (str[i] == prev) continue;
		prev = str[i];
		outstr += prev;
	}
	return outstr;
}
bool isValid(const char *str)
{
	std::string instr = compact(str);
	bool appeared[32] = {false};

	for(int i = 0; instr[i] != 0; i++){
		if (appeared[instr[i] - 'a']) return false;
		appeared[instr[i]-'a'] = true; 
	}
	return true;
}
void f(int size, const char *instr, bool *used)
{
	if (size == N){
		if(isValid(instr))
			answer++;
		return;
	}

	int i;
	char temp[3200]; 
	strcpy(temp, instr);
	int l = strlen(instr);
	for (i = 0; i < N; i++){
		if(used[i]) continue;
		used[i] = true;
		strcat(temp, str[i].c_str());
		f(size+1, temp, used);
		temp[l] = 0;
		used[i] = false;
	}
}
void solve(int caseNo)
{
	scanf("%d", &N);
	int i;
	for (i = 0; i < N; i++){
		std::cin>>str[i];
		str[i] = compact(str[i].c_str());
	}
	bool used[100] = {false};
	answer = 0;
	f(0, "", used);
	if (caseNo != 1)
		printf("\n");
	printf("Case #%d: %d", caseNo, answer);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
