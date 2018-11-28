#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int cases;
	cin>>cases;
	for (int c=0;c<cases;c++){
		cout<<"Case #"<<c+1<<": ";
		long long n;
		cin>>n;
		bool flag = false;
		bool visit[10];
		for (int i=0;i<10;i++) visit[i] = false;
		int j, k;
		k = 1000000000;
		j = 0;
					int tmp2 = n;
		while(flag == false && j < 100000){
			j++;
			int tmp = n;
			while(tmp > 0){
				visit[(tmp%10)]=true;
			//	cout<<tmp%10<<" ";
				tmp /= 10;
			}
			for (int i=0;i<10;i++){
				if (visit[i] == false) break;
				if (i == 9){
					flag = true;
					cout<<n<<"\n";
					break;
				}
			}
			n += tmp2;
			if (flag == false && (n > k || j > 99999)){
				cout<<"INSOMNIA\n";
				flag == true;
				break;
			}
		}
	}
	return 0;
}