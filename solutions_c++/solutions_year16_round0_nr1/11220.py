#include <iostream>
#include <set>
#include <string>

using namespace std;

int main(void){
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	int ct; cin >> ct;
	for(int caset=1;caset<=ct;caset++){
		int i=0, n, cont; cin >> n;
		set<int> myset;
		do{
			if(n==0)
				break;
			i++; cont = i*n;
			string num = to_string(cont);
			set<int>::iterator it;
			for(string::iterator is=num.begin(); is!=num.end(); is++)
				myset.insert(*is);
		}while(myset.size()!=10);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",caset);
		else
			printf("Case #%d: %d\n",caset, cont);
	}
	return 0; 
}

