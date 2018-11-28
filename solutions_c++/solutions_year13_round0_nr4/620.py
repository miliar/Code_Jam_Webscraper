#include <stdio.h>
#include <vector>
#include <map>

struct chest {

  std::vector<int> cont;
  int num;
  int key;

  chest(int num) {
    this->num = num;
    key = 0;
  }

};


std::vector<int> res_vec;
int level = 0;
bool impossible = false;
bool find_path(std::vector< chest * > *c, std::map<int, int> *k) {
 
  //printf("... \n");
 bool empty = true;
  for (int i =0 ; i < c->size(); i++) {
    if (c->at(i)) {
       empty=false; break;
    }
      
  }
  if (empty) return true;

  empty = true;
  int num = 0;
  int val = 0;
  int i = 0;
  for(std::map<int, int>::iterator it = k->begin(); it != k->end(); ++it ) {
    
    if (it->second!=0) { num++; val = i;  empty = false;  }
    i++;
  }
  if (num == 1 && c->at(val) &&  c->at(val)->cont.size() == 0) { impossible = true; return false; }; 
  if (empty) return false;

  for (int i =0 ; i < c->size(); i++) {
    //printf ("%d ... %d ///// \n", level, i);
    //if (c->at(i))
    //  printf("%d sprawdzam klucz %d do krzyni numer %d = %d\n",level, c->at(i)->key, i, (*k)[c->at(i)->key]);

    if (c->at(i) && (*k)[c->at(i)->key] > 0 ) {
      //printf("%d wykorzystuje klucz %d do krzyni numer %d\n",level, c->at(i)->key, i);
      (*k)[c->at(i)->key]--;
      chest *ch = c->at(i);
      c->at(i) = NULL;
      for (int j = 0; j < ch->cont.size(); j++) {
	(*k)[ch->cont[j]]++;
      }
      res_vec.push_back(i);
      level++;
      bool res = find_path(c,k);
      level--;
      if (res) return true;
      if (impossible) return false;
      res_vec.pop_back();
      c->at(i) = ch;
      (*k)[c->at(i)->key]++;
      for (int j = 0; j < ch->cont.size(); j++) {
	(*k)[ch->cont[j]]--;
      }
    }
  }
  //printf(" <<< \n");
  return false;
}

int main() {


  int T;
  scanf("%d", &T);

  int i = 0;

  while (T-- > 0) {
    res_vec.clear();
    int N, K;
    scanf("%d %d",  &K, &N);
    std::vector< chest *> chests;
    //chests.resize(N);
    std::map<int, int> keys;
    std::map<int, int> needed_keys;
    
    //printf("dostalem klucze : ");
    for (int j = 0; j < K; j++) {
      int key;
      scanf("%d", &key);
      //printf("%d", key);
      keys[key]++;
    }
    //printf("\n");

    for (int j = 0; j < N; j++) {
      //printf("setupuje skrzynie %d\n", j);
      int key_to_open;
      scanf("%d", &key_to_open);
      chest *c = new chest(j);
      c->key = key_to_open;
      needed_keys[key_to_open]++;
      int num;
      scanf("%d", &num);
      for (int k = 0; k < num; k++) {
	int cont;
	scanf("%d", &cont);
	c->cont.push_back(cont);
      }
      chests.push_back(c);
    }
   

    for (int k = 0; k < N; k++) {
      
      for (int w = 0; w < N; w++) {
	if (chests[w] && keys[chests[w]->key] > 0) {
	  bool has_sth_valuable = false;;
	  for (int x =0; x < chests[w]->cont.size(); x++) {
	    if (needed_keys[chests[w]->cont[x]] > 0) { has_sth_valuable=true; break;}
	  }
	  if (has_sth_valuable || keys[chests[w]->key] > 1 || needed_keys[chests[w]->key] == 1) {
	    //printf("otwieram %d\n", w);
	    
	    res_vec.push_back(w);
	    needed_keys[chests[w]->key]--;
	    keys[chests[w]->key]--;
	   
	    for (int x =0; x < chests[w]->cont.size(); x++) {
	      keys[chests[w]->cont[x]]++;
	    }
	    delete chests[w];
	    chests[w] = NULL;
	    break;
	  }
	  
	}

      }
      
    } 


    bool ok = true;
    for (int k = 0; k < N; k++) {
      if (chests[k]) { delete chests[k]; ok = false; }
    }
    
    printf("Case #%d: ", i+1);
    if (ok) {
      for (int w = 0; w < res_vec.size(); ++w) 
	printf("%d ",res_vec[w] + 1);
      printf("\n");
    } else {
      printf("IMPOSSIBLE\n");
    }
    
    i++;
  }



}
