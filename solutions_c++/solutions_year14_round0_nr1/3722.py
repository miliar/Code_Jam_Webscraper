#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <queue>
using namespace std;

typedef vector<int> voi;
typedef set<int> soi;
typedef vector<voi> vooi;
typedef pair<int, int> pii;

#define FOR(i, a, b) for(i=(a); i < (b); ++i)
#define REPEAT(i, n) FOR(i, 0, n)


int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	
	int n;
	scanf("%d", &n);
	int i,j,k;
	int c, d;
	int temp;
	soi s;
	int finded;
	bool exit;
	bool bad_mag = false;
	FOR(k, 1, n+1){
		printf("Case #%d: ", k);
		s.clear();
		exit = false;
		scanf("%d", &c);
		FOR(i, 1, 5){
			FOR(j, 1, 5){
				scanf("%d", &temp);
				if (i == c){
					s.insert(temp);
				}
			}
		}
		bad_mag = false;
		scanf("%d", &d);
		finded = -1;
		FOR(i, 1, 5){
			///if (exit)continue;
			FOR(j, 1, 5){
				scanf("%d", &temp);
				//if (exit)continue;
				if (i == d){
					if (s.find(temp) != s.end()){
						if (finded > 0){
							bad_mag = true;
							//exit = true;
							//continue;
						}
						else{
							finded = temp;
						}
					}
				}
			}
			
		}
		if (bad_mag){
			printf("Bad magician!\n");
		}
		else{
		if (finded > 0){
			printf("%d\n", finded);
		}
		else{
			printf("Volunteer cheated!\n");
		}
		}
	}

	return 0;
}
