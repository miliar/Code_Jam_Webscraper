#include <iostream>
#include <fstream>
int main(){
	std::ofstream out("out.txt");
	std::ifstream in("in.txt");
	int t, n;
	char status[10], flag;
	in >> t;
	for (int i = 1; i <= t; i++){
		std::fill(status, status + 10, 0);
		out << "Case #" << i << ": "; 
		in >> n;
		if (n == 0){
			out << "INSOMNIA\n";
		}
		else {
			int j, last, z;
			flag = 0;
			for (j = 1; flag < 10; j++){
				z = j * n;
				while (z){
					last = z % 10;
					if (!status[last]){
						status[last] = 1;
						flag++;
					}
					if (flag == 10){
						break;
					} 
					z = z / 10;
				}
			}
			out << (j - 1) * n << "\n";
		}
	}
	return 0;
}
