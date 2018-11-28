#include<iostream> 
#include<vector> 
#include<fstream>
#include<sstream>

using namespace std;

bool is_in_word(string word, char letter) {
	
	int cpt = 0;

        stringstream l;
        l << letter;

        string le;
        l >> le;

	while (cpt < word.size()) {

                stringstream ss;
                string s;

                ss << word[cpt];        
                ss >> s;

		if(le.compare(s) == 0)
			
			return true;
		
		cpt++;
		
	}
	
	return false;
	
}

string remove_word(string word, string lettres) {

        bool erase[lettres.size()];
       
        for(int i = 0; i < lettres.size(); i++) erase[i] = false;

        for(int i = 0; i < word.size(); i++) {

                for(int j = 0; j < lettres.size(); j++) {

                        if(i >= 0 && word[i] == lettres[j] && !erase[j]) {
                               
                                word.erase(i, 1);
                                erase[j] = true;
                                i--;

                        }

                }

        }        

        return word;

}

string maj_word(string word, char letter) {

        string lettres="";
                
        switch(letter) {

                case 'Z':
                        lettres = "ZERO";
                        word=remove_word(word, lettres);
                        break;
						
                case 'W':
                        lettres = "TWO";
                        word=remove_word(word, lettres);
                        break;
						
                case 'U':
                        lettres = "FOUR";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'X':
                        lettres = "SIX";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'G':
                        lettres = "EIGHT";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'O':
                        lettres = "ONE";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'H':
                        lettres = "THREE";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'F':
                        lettres = "FIVE";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'V':
                        lettres = "SEVEN";
                        word=remove_word(word, lettres);
                        break;
						
			   case 'N':
                        lettres = "NINE";
                        word=remove_word(word, lettres);
                        break;

                default:

                        break;

        }

        return word;

}

string get_phone(string word) {

        string phone = "";
        string even = "ZWUXG";
        string odd = "OHFVN";

        int is_in[10] = {0};

        // even numbers are uniquely defined
        for(int i = 0; i < 5; i++) {

                while(is_in_word(word, even[i])) {
				
                        for(int j = 0; j < word.size(); j++) {

                                if(word[j] == even[i]) {

                                        word = maj_word(word, even[i]);
                                        is_in[i*2]++;

                                }
						
			}

                }

        }

        // now the odd numbers are uniquely defined in the new word
        for(int i = 0; i < 5; i++) {

                // while the letter is present
                while(is_in_word(word, odd[i])) {
				
                 for(int j = 0; j < word.size(); j++) {

                         if(word[j] == odd[i]) {

                                word = maj_word(word, odd[i]);
                                is_in[(i*2)+1]++;

                        }

                }
				
                }

        }

        // word construction
        for(int i = 0; i < 10; i++) {

                while(is_in[i] > 0) {
                        
                        phone += to_string(i);
                        is_in[i]--;

                }

        }

        return phone;

}

int main(int argc, char** argv) {

        ifstream my_file;
        my_file.open(argv[1]);

        int T;
        my_file >> T;

        int cpt = 0;

        string ligne="";
        getline(my_file, ligne);

        while(cpt < T) {

                ligne ="";
                getline(my_file, ligne);

                cout << "Case #" << (cpt+1) << ": " << get_phone(ligne) << endl;

                cpt++;

        }

        my_file.close();

        return 0;

}
