#include<list>
#include<algorithm>
#include<cstdio>
using namespace std;


int main(){
	int q_casos;
	scanf("%d", &q_casos);
	for(int i = 0; i < q_casos; i++){
		int q_blocos;
		list<double> naomi_blocos;
		list<double> ken_blocos;
		scanf("%d", &q_blocos);
		for(int j = 0; j < q_blocos*2; j++){
			double bloco;
			scanf("%lf", &bloco);
			if(j < q_blocos)
				naomi_blocos.push_back(bloco);
			else
				ken_blocos.push_back(bloco);
		}
		//sort(naomi_blocos.begin(), naomi_blocos.end());
		//sort(ken_blocos.begin(), ken_blocos.end());
		naomi_blocos.sort();
		ken_blocos.sort();
		double blocon, blocok;
		int pontos_naomi = 0;
		list<double> kencp(ken_blocos.begin(), ken_blocos.end());
		list<double> nacp(naomi_blocos.begin(), naomi_blocos.end());
		for(int j = 0; j < q_blocos; j++){
			blocon = naomi_blocos.back();
			naomi_blocos.pop_back();
			list<double>::iterator it = upper_bound(ken_blocos.begin(), ken_blocos.end(), blocon);
			if(*it > blocon){
				blocok = *it;
				ken_blocos.remove(blocok);
			}else{
				blocok = ken_blocos.front();
				ken_blocos.pop_front();
				pontos_naomi++;
			}

		}
		double toldn, bna;
		int pontos_naomid = 0;
		for(int j = 0; j < q_blocos; j++){
			if(nacp.front() > kencp.front()){
				toldn = nacp.back() + 0.000001;
				bna = nacp.front();
				nacp.pop_front();
				blocon = toldn;
			}
			else if(nacp.front() < kencp.back()){
				//toldn = (kencp.at(-1) + kencp.at(-2))/2;
				toldn = kencp.back() - 0.000001;
				bna = nacp.front();
				nacp.pop_front();
				blocon = toldn;
			}else
			{
				blocon = nacp.back();
				nacp.pop_back();
				bna = blocon;
			}
			list<double>::iterator it = upper_bound(kencp.begin(), kencp.end(), blocon);
			if(*it > blocon){
				blocok = *it;
				kencp.erase(it);
			}else{
				blocok = kencp.front();
				kencp.pop_front();
				pontos_naomid++;
			}
			//printf("%lf %lf %lf\n", blocon, bna, blocok);


		}
		printf("Case #%d: %d %d\n",i+1,pontos_naomid, pontos_naomi);
	}
}
