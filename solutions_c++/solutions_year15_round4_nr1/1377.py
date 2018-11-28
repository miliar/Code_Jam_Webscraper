#include<iostream>
#include<vector>
#include<string>
#include<utility>

std::pair<int,int> searchArrow(const std::vector<std::string> &f, const int &x, const int &y, const int &vx, const int &vy){
	int p = x,q = y;
	p += vx, q += vy;
	const int mx = f[0].size();
	const int my = f.size();
	while(0 <= p && 0 <= q && p < mx && q < my){
		if(f[q][p] != '.'){
			return std::make_pair(p,q);
		}
		p += vx;
		q += vy;
	}
	return std::make_pair(-1,-1);
}

int main(){
	int t;
	std::cin >> t;
	for(int idT = 1; idT <= t; idT++){
		int x,y;
		std::cin >> y >> x;
		std::vector<std::string> field(y);
		int count = 0;
		bool possible = true;
		for(int i=0;i<y;i++)std::cin >> field[i];
		for(int i=0;i<x;i++){
			for(int j=0;j<y;j++){
				if(field[j][i] != '.'){
					int vx = 0, vy = 0;
					if(field[j][i] == '<')vx=-1,vy=0;
					if(field[j][i] == '>')vx=1,vy=0;
					if(field[j][i] == 'v')vx=0,vy=1;
					if(field[j][i] == '^')vx=0,vy=-1;
					auto p = searchArrow(field,i,j,vx,vy);
					if(p.first == -1){
						bool f=false;
						for(int k=0;k<3;k++){
							int px = -vy, py = vx;
							auto q = searchArrow(field,i,j,px,py);
							if(q.first != -1){
								f=true;
								break;
							}
							vx = px, vy = py;
						}
						if(f)count++;
						else possible = false;
					}
				}
				if(!possible)break;
			}
			if(!possible)break;
		}
		if(possible)std::cout << "Case #" << idT << ": " << count << std::endl;
		else std::cout << "Case #" << idT << ": IMPOSSIBLE" << std::endl;
	}
	return 0;
}