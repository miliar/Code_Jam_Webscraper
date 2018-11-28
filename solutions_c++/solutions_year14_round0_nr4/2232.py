#include <iostream>
#include <fstream>
#include <list>

void get_list(std::list<double>& pieces, const long& n_pieces, std::ifstream& input) {
	for (long p = 0; p < n_pieces; ++p) {
		double mass = 0;
		input >> mass;
		pieces.push_back(mass);
	}
}

using std::cout; using std::endl;
int main() {
	std::ifstream input;
	input.open("./data/D-large.in");
	std::ofstream out;
	out.open("./data/D-large.out");
	long cases;
	input >> cases;

	std::cout << cases << std::endl;
	for (long c = 0; c < cases; ++c) {
		long n_pieces = 0;
		input >> n_pieces;
		std::list<double> pieces_ken;
		std::list<double> pieces_naomie;
		
		get_list(pieces_naomie, n_pieces, input);
		get_list(pieces_ken, n_pieces, input);

		pieces_ken.sort();
		pieces_naomie.sort();

		std::list<double> pieces_naomie_lie{pieces_naomie};
		std::list<double> pieces_ken_lie{pieces_ken};
		long n_pts_deceit = 0;
		long n_pts_truth = 0;

		while(!pieces_ken.empty()) { // have to simulate this, I guess =(
			double m_truth = pieces_naomie.back();
			pieces_naomie.pop_back();
			double m_ken_truth = 0;
			auto it_sel = pieces_ken.end();
			
			for (auto it = pieces_ken.begin(); it != pieces_ken.end(); ++it) {
				if (*it > m_truth) { 
					m_ken_truth = *it;
					it_sel = it;
					break;
				}
			}
			if (it_sel == pieces_ken.end()) {
				m_ken_truth = pieces_ken.front();
				pieces_ken.pop_front();
			}
			else {
				pieces_ken.erase(it_sel);
			}

			if (m_ken_truth < m_truth) ++n_pts_truth;


			double m_lie = 0;
			if (pieces_naomie_lie.back() > pieces_ken_lie.back()) {
				m_lie = pieces_naomie_lie.back();
				pieces_naomie_lie.pop_back();
			} else {
				m_lie = pieces_naomie_lie.front();
				pieces_naomie_lie.pop_front();
			}
			double m_ken_lie = 0;
			m_ken_lie = pieces_ken_lie.back();
			pieces_ken_lie.pop_back();
			cout << m_lie << " " << m_ken_lie << endl;
			if (m_ken_lie < m_lie) ++n_pts_deceit;


		}
		cout<< "Case #" << c+1 << ": " << n_pts_deceit << " " << n_pts_truth << endl; 
		out << "Case #" << c+1 << ": " << n_pts_deceit << " " << n_pts_truth << endl;
	}
	input.close();
	out.close();
}