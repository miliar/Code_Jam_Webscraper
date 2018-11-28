#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <cmath>
#define pi 3.14159265359
using namespace std;

int main(){

	int n, r, t, c, x, us;
	scanf("%d", &n);
	int area, preto, area2;
	
	for(int i = 1; i <= n ;i++){
		scanf("%d %d", &r, &t);
		c = x = 0;
		
		us = t;
		while(true){
			
			area = r * r;
		
			r = r + 1;			
			area2 = r * r;
		
			r = r + 1;
			
			preto = area2 - area;
			
			if(preto <= us){
				c++;
				us -= preto;
			}else{
				break;
			}
			
		}
		printf("Case #%d: %d\n", i, c);
	}
	return 0;
}