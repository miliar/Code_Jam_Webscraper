#include <iostream>
#include <vector>
#include <algorithm>

double MAX(double a, double b) {
	if (a - b > 0) {
		return a;
	} else {
		return b;
	}
}

void input(std::vector<float> &vec) {
    for(int i = 0; i < vec.size(); i++)
        std::cin >> vec[i];
    std::sort(vec.begin(), vec.end());
}

int getIndexToDelete(const std::vector<float> &vec, float val) {
    //std::cout <<"value in Naomi: " << val <<"  ";
    int N = vec.size();
    if (val > vec[N-1])
        return 0;
    for (int i = 0; i < N; i++) {
        if (val < vec[i]) {
            //std::cout << "Ken : " << vec[i] <<"\n";
            return i;
        }
    }
}

int getWinInWar(std::vector<float> naomi, std::vector<float> ken) {
    int winCount = 0;
    int N = naomi.size();
    for(int i = 0; i < N; i++) {
        float val = naomi[i];
        int j = getIndexToDelete(ken, val);
        if (val > ken[j]) {
            winCount ++;
        }
        ken.erase(ken.begin()+j, ken.begin()+j+1);
    }
    return winCount;
}

float getSum(const std::vector<float> &ken) {
    int N = ken.size();
    float sum = 0;
    for (int i = 0; i < N; i ++)
        sum += ken[i];
    return sum;
}

int getWinInDeceitfulWar(std::vector<float> naomi, std::vector<float> ken) {
    int winCount = 0;
    int N = naomi.size();
    for(int i = 0; i < N; i++) {
        float val = naomi[i];
        int ind;
        if (val < ken[0]) {
            ind = ken.size() - 1;
        } else {
            ind = 0;
            winCount ++;
        }
        ken.erase(ken.begin()+ind, ken.begin()+ind+1);
        /*int j = getIndexToDelete(ken, val);
        std::cout << "sum = " << sum <<" avg = " << avg << "  naomi[i] = " << naomi[i] <<"  ken[j] = " << ken[j] <<"\n";
        if (naomi[i] > ken[j]) {
            winCount ++;
        }
        ken.erase(ken.begin()+j, ken.begin()+j+1);*/
    }
    return winCount;
}

void print(const std::vector<float> &vec) {
    for(int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\n";
}

int main() {
    int T;
    std::cin >> T;
    for (int t =1 ; t <=T; t++) {
        int N;
        std::cin >> N;
        std::vector<float> naomi(N), ken(N);
        input(naomi);
        input(ken);
        //print(naomi);print(ken);
        int win1 = getWinInDeceitfulWar(naomi, ken);
        int win2 = getWinInWar(naomi, ken);
        std::cout <<"Case #" << t << ": " << win1 << " " << win2 <<"\n";;
    }
    return 0;
}
