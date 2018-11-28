#include <iostream>
#include <limits>
#include <cstdio>
using namespace std;

int main(int argc, char **argv)
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int times;
	cin >> times;
	for(int t = 1; t <= times; t++){
		cin.ignore(numeric_limits<streamsize>::max(),'\n');
		string p1, p2;
		cin >> p1 >> p2;
		int s1, s2;
		s1 = p1.size();
		s2 = p2.size();
		int p1i, p2i;
		p1i =-1;
		p2i = 1000;
		int ts = p1.size();
		for(int i = 0; i < (int)(3-ts); i++){
			p1.insert(p1.begin(), '0');
			p2.insert(p2.begin(), '0');
		}
	//	cout << p1.size() << " " << p2 << ":::" << endl;
		for(int i1 = 0; i1 <= 9; i1++){
			if(p1[0] != '?' && p1[0]-'0' != i1) continue;
			for(int i2 = 0; i2 <= 9; i2++){
				if(p1[1] != '?' && p1[1]-'0' != i2) continue;
				for(int i3 = 0; i3 <= 9; i3++){
					if(p1[2] != '?' && p1[2]-'0' != i3) continue;
					for(int i4 = 0; i4 <= 9; i4++){
						if(p2[0] != '?' && p2[0]-'0' != i4) continue;
						for(int i5 = 0; i5 <= 9; i5++){
							if(p2[1] != '?' && p2[1]-'0' != i5) continue;
							for(int i6 = 0; i6 <= 9; i6++){
								if(p2[2] != '?' && p2[2]-'0' != i6) continue;
								//cout << i1 << " " << i2 << " " << i3 << " " << i4 << " " << i5 << " " << i6 << endl;
								int t1,t2;
								t1 = i1*100 + 10*i2+i3;
								t2 = i4 *100 + 10 * i5 + i6;
						//		cout << t1 << " " << t2 << endl;
							//	cout << p2i << " "<< p1i << " " << abs(p2i-p1i) << endl;
								if(abs(t2-t1) < abs(p2i-p1i)){
									p1i = t1;
									p2i = t2;
								}else if(abs(t2-t1) == abs(p2i-p1i)){
									if(t1 < p1i){
										p1i = t1;
										p2i = t2;
									}else if( t1 == p1i){
										if(t2 < p2i){
											p1i = t1;
											p2i = t2;
										}
									}
								}
							}
						}
					}
				}
			}
		}
		cout << "Case #" << t << ": ";
		if(p1i < 10 && s1 == 3) cout << "00";
		else if((p1i < 100 && s2 > 2) || (p1i < 10 && s1 == 2)) cout << "0";
		cout << p1i << " ";
		if(p2i < 10 && s1 == 3) cout << "00";
		else if((p2i < 10 && s1 == 2) || (p2i < 100 && s1 > 2)) cout << "0";
		cout << p2i << endl;
	}
	
							
	return 0;
}

