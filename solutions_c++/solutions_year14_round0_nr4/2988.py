#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

struct NaomiChosenAndTold {
	double chosen;
	double told;
};

class War {
protected:
	vector<double> _naomis, _kens;
	const size_t _N;

	double chosenKen(double told_naomi) {
		size_t chosen_index(0);
		if (_kens.back() > told_naomi) {
			chosen_index = lower_bound(_kens.begin(), _kens.end(), told_naomi) -
				_kens.begin();
		}
		double result = _kens[chosen_index];
		_kens.erase(_kens.begin() + chosen_index);
		return result;
	}

	virtual NaomiChosenAndTold chosenAndToldNaomi() {
		NaomiChosenAndTold result = {0, };
		result.chosen = result.told = _naomis.back();
		_naomis.pop_back();
		return result;
	}

public:
	War(vector<double> naomis, vector<double> kens):
		_naomis(naomis), _kens(kens), _N(naomis.size())
	{ }

	int play() {
		int naomis_score(0);
		for (size_t i = 0; i < _N; i++) {
			NaomiChosenAndTold naomi = chosenAndToldNaomi();
			double chosen_ken = chosenKen(naomi.told);
			if (naomi.chosen > chosen_ken) naomis_score++;
		}
		return naomis_score;
	}
};


class DeceitfulWar: public War {
private:
	NaomiChosenAndTold chosenAndToldNaomi() {
		NaomiChosenAndTold naomi = {0, };
		if (_naomis.size() > 1) {
			for (size_t i = 0; i < _naomis.size(); i++) {
				if (_naomis[i] > _kens[0]) {
					naomi.chosen = _naomis[i];
					_naomis.erase(_naomis.begin() + i);
					naomi.told = _kens.back() + 1;
					return naomi;
				}
			}
			naomi.chosen = _naomis[0];
			double a = _kens[_kens.size() - 1];
			double b = _kens[_kens.size() - 2];
			naomi.told = a + (b - a) / 2.0;
			_naomis.erase(_naomis.begin());
		}
		else
		{
			naomi.chosen = naomi.told = _naomis[0];
			_naomis.erase(_naomis.begin());
		}
		return naomi;
	}

public:
	DeceitfulWar(vector<double> naomis, vector<double> kens):
		War(naomis, kens)
	{ }
};


int main()
{
	int T(0), t(0), N(0), i(0);
	vector<double> naomis, kens;

	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cin >> N;
		naomis.clear();
		naomis.resize(N);
		kens.clear();
		kens.resize(N);
		for (i = 0; i < N; i++) cin >> naomis[i];
		for (i = 0; i < N; i++) cin >> kens[i];
		sort(naomis.begin(), naomis.end());
		sort(kens.begin(), kens.end());
		DeceitfulWar deceitful_war(naomis, kens);
		War war(naomis, kens);
		cout << "Case #" << t << ": " << deceitful_war.play() << " " <<
			war.play() << endl;
	}
	return 0;
}
