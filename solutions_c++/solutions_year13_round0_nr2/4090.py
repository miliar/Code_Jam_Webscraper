#include <iostream>
#include <string>
#include <vector>

using namespace std;

// bool verifDirection (vector<vector<int>> & gazon, int ligne, int colonne,
// 		     int deplacementVertical, int deplacementHorizontal)
// {
//   int tailleCase = gazon[ligne][colonne];

//   ligne += deplacementVertical;
//   colonne += deplacementHorizontal;

//   while (gazon[ligne][colonne] != 0) {
//     if (gazon[ligne][colonne] > tailleCase) {
//       return false;
//     }

//     ligne += deplacementVertical;
//     colonne += deplacementHorizontal;
//   }

//   return true;
// }

// bool verifCase (vector<vector<int>> & gazon, int ligne, int colonne)
// {
//   return
//     verifDirection(gazon, ligne, colonne,  1,  0) ||
//     verifDirection(gazon, ligne, colonne, -1,  0) ||
//     verifDirection(gazon, ligne, colonne,  0,  1) ||
//     verifDirection(gazon, ligne, colonne,  0, -1);
// }

bool possible (vector<vector<int>> & gazon, int nbLignes, int nbColonnes)
{
  vector<vector<int>> simulation;

  for (int i = 0; i < nbLignes; ++i) {
    int max = 0;
    for (int j = 0; j < nbColonnes; j++) {
      max = (max < gazon[i][j]) ? gazon[i][j] : max;
    }

    simulation.push_back(vector<int>(nbColonnes, max));
  }

  for (int j = 0; j < nbColonnes; j++) {
    int max = 0;
    for (int i = 0; i < nbLignes; i++) {
      max = (max < gazon[i][j]) ? gazon[i][j] : max;
    }

    for (int i = 0; i < nbLignes; i++) {
      simulation[i][j] = (simulation[i][j] < max) ? simulation[i][j] : max;
      if (simulation[i][j] != gazon[i][j]) {
	return false;
      }
    }
  }

  return true;
}

int main(int argc, char** argv)
{
  int nbTests;

  cin >> nbTests;

  for(int i = 0; i < nbTests; i++){
    int nbLignes, nbColonnes;
    cin >> nbLignes >> nbColonnes;

    vector<vector<int>> gazon;

    // gazon.push_back(vector<int>(nbColonnes + 2, 0));

    for (int i = 0; i < nbLignes; i++) {
      vector<int> temp;
      // temp.push_back(0);
      for (int j = 0; j < nbColonnes; j++) {
	int hauteur;
	cin >> hauteur;

	temp.push_back(hauteur);
      }
      // temp.push_back(0);
      gazon.push_back(temp);
    }
    // gazon.push_back(vector<int>(nbColonnes + 2, 0));

    cout << "Case #" << i + 1 << ": ";

    if (possible(gazon, nbLignes, nbColonnes)) {
      cout << "YES";
    }
    else {
      cout << "NO";
    }

    cout << endl;
  }

  return 0;
}
