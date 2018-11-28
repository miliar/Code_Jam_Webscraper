#include <fstream>
#include <iostream>
#include <set>

int play_war(std::set<double>& naomi, std::set<double>& ken) {
    int naomis_points=0;
    // Naomi picks largest first
    for(std::set<double>::reverse_iterator it=naomi.rbegin(); it!=naomi.rend(); ++it) {
        // Ken chooses next larger if possible, else smallest
        std::set<double>::iterator kens_play=ken.lower_bound(*it);
        if(kens_play!=ken.end()) {
            ken.erase(kens_play);
        } else {
            ++naomis_points;
            ken.erase(ken.begin());
        }

    }
    return naomis_points;
}

int play_deceitful_war(std::set<double>& naomi, std::set<double>& ken) {
    int naomis_points=0;
    // Naomi picks smallest first
    for(std::set<double>::iterator it=naomi.begin(); it!=naomi.end(); ++it) {
        // Naomi tries to beat one of kens blocks, else she makes him use his largest block
        std::set<double>::iterator beat_this=ken.upper_bound(*it);
        if(beat_this==ken.end()) {
            ken.erase(ken.begin());
            ++naomis_points;
        } else if(beat_this!=ken.begin()) {
            --beat_this;
            ken.erase(beat_this);
            ++naomis_points;
        } else {
            beat_this=ken.end();
            --beat_this;
            ken.erase(beat_this);
        }
    }
    return naomis_points;
}

int main() {
    std::ifstream infile("input.txt");
	std::ofstream outfile("output.txt");

	int testcases;
	infile>>testcases;

    int N;
    double value;
    std::set<double> naomi;
    std::set<double> ken;
    std::set<double> ken_deceitful;

	for(int i=1; i<=testcases; ++i) {
        infile>>N;
        naomi.clear();
        for(int j=0; j<N; ++j) {
            infile>>value;
            naomi.insert(value);
        }
        ken.clear();
        ken_deceitful.clear();
        for(int j=0; j<N; ++j) {
            infile>>value;
            ken.insert(value);
            ken_deceitful.insert(value);
        }
        outfile<<"Case #"<<i<<": "<<play_deceitful_war(naomi, ken_deceitful)<<" "<<play_war(naomi, ken)<<std::endl;
	}

    return 0;
}
