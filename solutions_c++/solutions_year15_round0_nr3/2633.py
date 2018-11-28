// i wish i remembered how to use yacc/bison!!!!!
// lets see if i can just program it :)
// for ndfa with states below....
#include <iostream>
#include <fstream>
#include <set>
#include <string>
using namespace std;

enum state {
  I,         J,         K,         ONE,         NEG_I,         NEG_J,         NEG_K,         NEG_ONE,         // 8
  I_DONE_I,  I_DONE_J,  I_DONE_K,  I_DONE_ONE,  I_DONE_NEG_I,  I_DONE_NEG_J,  I_DONE_NEG_K,  I_DONE_NEG_ONE,  //16
  IJ_DONE_I, IJ_DONE_J, IJ_DONE_K, IJ_DONE_ONE, IJ_DONE_NEG_I, IJ_DONE_NEG_J, IJ_DONE_NEG_K, IJ_DONE_NEG_ONE, NULLS //24
};

pair<state, state> getStepStates(state currentState, char c) {
  switch(currentState) {
    case ONE:
          if (c == 'i') return make_pair(I, I_DONE_ONE);
          if (c == 'j') return make_pair(J, NULLS);
          if (c == 'k') return make_pair(K, NULLS);
    case I:
          if (c == 'i') return make_pair(NEG_ONE, NULLS);
          if (c == 'j') return make_pair(K, NULLS);
          if (c == 'k') return make_pair(NEG_J, NULLS);
    case J:
          if (c == 'i') return make_pair(NEG_K, NULLS);
          if (c == 'j') return make_pair(NEG_ONE, NULLS);
          if (c == 'k') return make_pair(I, I_DONE_ONE);
    case K:
          if (c == 'i') return make_pair(J, NULLS);
          if (c == 'j') return make_pair(NEG_I, NULLS);
          if (c == 'k') return make_pair(NEG_ONE, NULLS);
    case NEG_ONE:
          if (c == 'i') return make_pair(NEG_I, NULLS);
          if (c == 'j') return make_pair(NEG_J, NULLS);
          if (c == 'k') return make_pair(NEG_K, NULLS);
    case NEG_I:
          if (c == 'i') return make_pair(ONE, NULLS);
          if (c == 'j') return make_pair(NEG_K, NULLS);
          if (c == 'k') return make_pair(J, NULLS);
    case NEG_J:
          if (c == 'i') return make_pair(K, NULLS);
          if (c == 'j') return make_pair(ONE, NULLS);
          if (c == 'k') return make_pair(NEG_I, NULLS);
    case NEG_K:
          if (c == 'i') return make_pair(NEG_J, NULLS);
          if (c == 'j') return make_pair(I, I_DONE_ONE);
          if (c == 'k') return make_pair(ONE, NULLS);
    /////////////////////////////////////////////////////////  found I
    case I_DONE_ONE:
          if (c == 'i') return make_pair(I_DONE_I, NULLS);
          if (c == 'j') return make_pair(I_DONE_J, IJ_DONE_ONE);
          if (c == 'k') return make_pair(I_DONE_K, NULLS);
    case I_DONE_I:
          if (c == 'i') return make_pair(I_DONE_NEG_ONE, NULLS);
          if (c == 'j') return make_pair(I_DONE_K, NULLS);
          if (c == 'k') return make_pair(I_DONE_NEG_J, NULLS);
    case I_DONE_J:
          if (c == 'i') return make_pair(I_DONE_NEG_K, NULLS);
          if (c == 'j') return make_pair(I_DONE_NEG_ONE, NULLS);
          if (c == 'k') return make_pair(I_DONE_I, NULLS);
    case I_DONE_K:
          if (c == 'i') return make_pair(I_DONE_J, IJ_DONE_ONE);
          if (c == 'j') return make_pair(I_DONE_NEG_I, NULLS);
          if (c == 'k') return make_pair(I_DONE_NEG_ONE, NULLS);
    case I_DONE_NEG_ONE:
          if (c == 'i') return make_pair(I_DONE_NEG_I, NULLS);
          if (c == 'j') return make_pair(I_DONE_NEG_J, NULLS);
          if (c == 'k') return make_pair(I_DONE_NEG_K, NULLS);
    case I_DONE_NEG_I:
          if (c == 'i') return make_pair(I_DONE_ONE, NULLS);
          if (c == 'j') return make_pair(I_DONE_NEG_K, NULLS);
          if (c == 'k') return make_pair(I_DONE_J, IJ_DONE_ONE);
    case I_DONE_NEG_J:
          if (c == 'i') return make_pair(I_DONE_K, NULLS);
          if (c == 'j') return make_pair(I_DONE_ONE, NULLS);
          if (c == 'k') return make_pair(I_DONE_NEG_I, NULLS);
    case I_DONE_NEG_K:
          if (c == 'i') return make_pair(I_DONE_NEG_J, NULLS);
          if (c == 'j') return make_pair(I_DONE_I, NULLS);
          if (c == 'k') return make_pair(I_DONE_ONE, NULLS);	  
    /////////////////////////////////////////////////////////  found IJ	  
    case IJ_DONE_ONE:
          if (c == 'i') return make_pair(IJ_DONE_I, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_J, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_K, NULLS);
    case IJ_DONE_I:
          if (c == 'i') return make_pair(IJ_DONE_NEG_ONE, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_K, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_NEG_J, NULLS);
    case IJ_DONE_J:
          if (c == 'i') return make_pair(IJ_DONE_NEG_K, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_NEG_ONE, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_I, NULLS);
    case IJ_DONE_K:
          if (c == 'i') return make_pair(IJ_DONE_J, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_NEG_I, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_NEG_ONE, NULLS);
    case IJ_DONE_NEG_ONE:
          if (c == 'i') return make_pair(IJ_DONE_NEG_I, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_NEG_J, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_NEG_K, NULLS);
    case IJ_DONE_NEG_I:
          if (c == 'i') return make_pair(IJ_DONE_ONE, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_NEG_K, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_J, NULLS);
    case IJ_DONE_NEG_J:
          if (c == 'i') return make_pair(IJ_DONE_K, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_ONE, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_NEG_I, NULLS);
    case IJ_DONE_NEG_K:
          if (c == 'i') return make_pair(IJ_DONE_NEG_J, NULLS);
          if (c == 'j') return make_pair(IJ_DONE_I, NULLS);
          if (c == 'k') return make_pair(IJ_DONE_ONE, NULLS);
    /////////////////////////////////////////////////////////  ERROR
    case NULLS:
          if (c == 'i') return make_pair(NULLS, NULLS);
          if (c == 'j') return make_pair(NULLS, NULLS);
          if (c == 'k') return make_pair(NULLS, NULLS);
      
  };
}

int main () {
  ifstream fin("in.txt");
  ofstream fout("out.txt");
  int cases = 0;
  set<state> setone;
  set<state> settwo;
  set<state> * eval; 
  set<state> * build;

  fin >> cases;
  for (int i = 1; i <= cases; ++i) {
    string s;
    int size, reps;
    fin >> size >> reps;
    fin >> s;
    string ss = "";
    while(reps--) {
      ss = ss + s;
    };
    fout << "Case #" << i << ": ";
    
    eval = &setone;
    build = &settwo;
    eval[0].insert(ONE);
    for (size_t i = 0; i < ss.length(); ++i) {
      while(!(*eval).empty()) {
        state evalState = *(*eval).begin();
        (*eval).erase((*eval).begin());
        pair<state, state> nextStates = getStepStates(evalState, ss[i]);
        (*build).insert(nextStates.first);
        if (nextStates.second != NULLS)
          (*build).insert(nextStates.second);
        if ((*build).size() == 23) {
          // if eval ! empty but build.size == full then empty current and continue
          break;
        }
      }
      set<state> * tmp = eval;
      eval = build;
      build = tmp;
    };
    if ((*eval).find(IJ_DONE_K) != (*eval).end()) 
      fout << "YES\n";
    else fout << "NO\n";
    while (!(*eval).empty()) 
      (*eval).erase((*eval).begin());
    while (!(*build).empty()) 
      (*build).erase((*build).begin());
  }
  fin.close();
  fout.close();

}
