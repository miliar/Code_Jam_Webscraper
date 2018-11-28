#include<cstdio>
#include<algorithm>
#include<string>

using namespace std;

int main(){
	int casos;
	char f, aux[2000];
	string s, vor, nach;
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
		scanf(" %s", aux); s = aux;
		f = s[0];
		vor = nach = "";
		for(int i=1;i<s.size();i++){
			if(s[i] >= f){
				f = s[i];
				vor += s[i];
			}
			else{
				nach += s[i];
			}
		}
		
		printf("Case #%d: ", inst);
		for(int i=vor.size()-1;i>=0;i--) printf("%c", vor[i]);
		printf("%c%s\n", s[0], nach.c_str());
	}
	return 0;
}
