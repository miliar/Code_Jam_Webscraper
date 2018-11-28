#include <iostream>
#include <vector>

int main(){
	int n;
	
	std::cin >> n;
	for(int t=0;t<n;t++){
		std::cout << "Case #"<< t+1 << ": ";

		int ans;
		std::cin >> ans;
		ans--;
		std::vector<std::vector<int>> val(4, std::vector<int>(4));
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				std::cin >> val[i][j];
			}
		}

		std::vector<int> candidates= val[ans];

//		std::for_each(candidates.begin(),candidates.end(),[](int a){
//				std:: cout << a << " ";
//				});
//		std::cout << std::endl;

		std::cin >> ans;
		ans--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				std::cin >> val[i][j];
			}
		}

		//cheat
		std::vector<int> candidates2=val[ans];
		//for(int i=0;i<4;i++) std::cout << candidates[i] << " ";
		//std::cout << std::endl;
		//for(int i=0;i<4;i++) std::cout << candidates2[i] << " ";
		//std::cout << std::endl;
		bool isCheat=true;
		int result;
		int c=0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(candidates[i]==candidates2[j]){
					c+=1;
					result=candidates[i];
					isCheat=false;
				}
			}
		}
		if(isCheat){
			std::cout << "Volunteer cheated!" << std::endl;
			continue;
		}
		if(c!=1){
			std::cout << "Bad magician!" << std::endl;
			continue;
		}
		std::cout << result << std::endl;

	}

	return 0;
}
