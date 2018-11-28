#include <stdio.h>
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int table(char x){
	if(x == '1')
		return 0;
	if(x == 'i')
		return 1;
	if(x == 'j')
		return 2;
	if(x == 'k')
		return 3;
	return -1;
}

string quaternion[4][4] = 
	{{"1", "i", "j", "k"}, {"i", "-1", "k", "-j"}, {"j", "-k", "-1", "i"}, {"k", "j", "-i", "-1"}};

string prod(string x, string y){
	if(x[0] == '-' && y[0] == '-')
		return quaternion[table(x[1])][table(y[1])];
	if(x[0] == '-' || y[0] == '-'){
		if(x[0] == '-'){
			if(quaternion[table(x[1])][table(y[0])][0] == '-')
				return quaternion[table(x[1])][table(y[0])].substr(1, 1);
			else
				return "-" + quaternion[table(x[1])][table(y[0])];
		}
		else{
			if(quaternion[table(x[0])][table(y[1])][0] == '-')
				return quaternion[table(x[0])][table(y[1])].substr(1, 1);
			else
				return "-" + quaternion[table(x[0])][table(y[1])];
		}
	}
	else
		return quaternion[table(x[0])][table(y[0])];
}

string Prod(string x){
	int l = x.size();
	string y = x.substr(0, 1);
	for(int i = 1; i < l; i++)
		y = prod(y, x.substr(i, 1));
	return y;
}

queue <int> Find(string x, string y, int length, int offset){
	queue <int> Q;
	string s = x.substr(0, 1);
	for(int i = 1; i < length; i++){
		if(s == y)
			Q.push(i + offset);
		s = prod(s, x.substr(i, 1));
	}
	return Q;
}

int main(){

	int T, L, X, case1 = 1, i, l, flag, x, y;
	string s, s2, eval;
	scanf("%d", &T);
	while(T--){
		scanf("%d %d", &L, &X);
		cin >> s;
		eval = Prod(s);
		if((eval == "-1" && (X % 2 == 1)) || (eval != "1" && ((X - 2) % 4 == 0))){
			s2 = "";
			for(i = 0; i < X; i++)
				s2 += s;
			l = L*X;
			flag = 1;
			queue <int> Qi = Find(s2, "i", l, 0);
			while(!Qi.empty() && flag){
				x = Qi.front();
				Qi.pop();
				queue <int> Qj = Find(s2.substr(x, l - x), "j", l - x, x);
				while(!Qj.empty() && flag){
					y = Qj.front();
					Qj.pop();
					if(Prod(s2.substr(y, l - y)) == "k")
						flag = 0;
				}
			}
			if(flag == 0)
				printf("Case #%d: YES\n", case1);
			else
				printf("Case #%d: NO\n", case1);
		}
		else
			printf("Case #%d: NO\n", case1);
		case1++;
	}
	return 0;
}