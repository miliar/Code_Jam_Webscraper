#include<fstream>
#include<string.h>
using namespace std;

bool alltrue(bool* num){
	for (int i = 0; i < 10; i++)
		if (!num[i]) return false;
	return true;
}

void setnum(int n, bool* num){
	while (n > 0){
		num[n % 10] = true;
		n = n /10;
	}
	return;
}

int main(){
	int t,n,tmp;
	ifstream in("A-large.in");
	in >> t;
	bool num[10];
	ofstream out("Sheep.out");
	for (int i = 0; i < t; i++){
		in >> n;
		if (n == 0){
			out << "Case #" << i+1 <<": INSOMNIA" << endl;
			continue;
		}
		tmp = 0;
		memset(num,false,sizeof(num));
		while (!alltrue(num)){
			tmp = tmp + n;
			setnum(tmp,num);
		}
		out << "Case #" << i+1 << ": " << tmp << endl;
	}
	in.close();
	out.close();
	return 0;
}
