#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int T,n,cek,move;
	vector<int> num;
	vector<char> cha;
	char ch,tmp;
	scanf("%d",&T);
	for(int z=1;z<=T;z++) {
		num.clear();
		cha.clear();
		scanf("%d",&n);
		ch = getchar();
		ch = getchar();
		tmp = ch;
		n = 1;
		ch = getchar();
		while(ch!='\n') {
			if(ch==tmp) n++;
			else {
				num.push_back(n);
				cha.push_back(tmp);
				n = 1;
				tmp = ch;
			}
			ch = getchar();
		}
		num.push_back(n);
		cha.push_back(tmp);
		ch = getchar();
		n = 1;
		cek = 0;
		move = 0;
		if(ch!=cha[0]) printf("Case #%d: Fegla Won\n",z);
		else {
			tmp = ch;
			while(1) {
				if(cek >= num.size()) {
					move = -1;
					break;
				}
				ch = getchar();
				if(ch == '\n') {
					if(cek < num.size()-1) {
						move = -1;
						break;
					}
					if(tmp != cha[cek]) { 
						move = -1;
						break;
					}
					if(num[cek]>n) move += num[cek]-n;
					else move += n-num[cek];
					cek++;
					tmp = ch;
					n = 1;
					break;
				}
				if(ch!=tmp) {
					if(tmp == cha[cek]) {
						if(num[cek]>n) move += num[cek]-n;
						else move += n-num[cek];
						cek++;
						tmp = ch;
						n = 1;
					}
					else {
						move = -1;
						break;
					}
				}
				else n++;
			}
			if(move==-1) printf("Case #%d: Fegla Won\n",z);
			else printf("Case #%d: %d\n",z,move);
		}
		while(ch!='\n') ch = getchar();                          
	}
	return 0;
}
						
			
